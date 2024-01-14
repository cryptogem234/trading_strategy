import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash_table import DataTable
import pandas as pd
import total_strategies as ts
from datetime import datetime

# Create Dash app
app = dash.Dash(__name__)
server = app.server

# Initialize dataframes
col_list = ['strategy_name','date','ticker','close','pctreturn']
tqqq_or_not = pd.DataFrame(columns=col_list)
rat_ftlt = pd.DataFrame(columns=col_list)
nothing_but_bonds = pd.DataFrame(columns=col_list)
short_volatility_svxy = pd.DataFrame(columns=col_list)
wam_ftlt = pd.DataFrame(columns=col_list)

# Define a list of dictionaries for each table
tables = [
    {'id': 'tqqq_or_not', 'df': tqqq_or_not, 'button_id': 'refresh-button', 'name': 'TQQQ or Not'},
    {'id': 'rat_ftlt', 'df': rat_ftlt, 'button_id': 'refresh-button2', 'name': 'RAT FTLT'},
    {'id': 'nothing_but_bonds', 'df': nothing_but_bonds, 'button_id': 'refresh-button3', 'name': 'Nothing but Bonds'},
    {'id': 'short_volatility_svxy', 'df': short_volatility_svxy, 'button_id': 'refresh-button4', 'name': 'Short Volatility SVXY'},
    {'id': 'wam_ftlt', 'df': wam_ftlt, 'button_id': 'refresh-button5', 'name': 'WAM FTLT'}
]

# Define layout dynamically
layout = [html.H1("Strategies List")]

# Add Dash DataTable components for each table dynamically
for table in tables:
    layout.extend([
        html.H2(table['name'], style={'font-size': '1.5rem', 'margin-bottom': '0'}),
        DataTable(
            id=table['id'],
            columns=[{'name': col, 'id': col} for col in table['df'].columns],
            data=table['df'].to_dict('records'),
            style_cell={'minWidth': '100px', 'maxWidth': '100px', 'textAlign': 'left'},
        ),
        html.Div([
            html.Span("Last Refresh: ", style={'margin-right': '10px'}),
            html.Span(id=f"refresh-time-{table['id']}", style={'margin-right': '20px'}),
            html.Button("Refresh Data", id=table['button_id'], n_clicks=0),
            dcc.Loading(id=f"loading-{table['id']}", type="circle", children=[]),
        ]),
        html.Hr()  # Add a horizontal line for separation after each table
    ])

# Define callbacks dynamically
for table in tables:
    @app.callback(
        [Output(table['id'], 'data'),
         Output(f"loading-{table['id']}", 'children'),
         Output(f"refresh-time-{table['id']}", 'children')],
        [Input(table['button_id'], 'n_clicks')],
        [State(f"loading-{table['id']}", 'children')],
        prevent_initial_call=True
    )
    def update_output(n_clicks, children, table=table):
        if n_clicks > 0:
            # Replace dashes with underscores in the table ID
            function_name = f"execute_{table['id'].replace('-', '_')}_strategy"
            result_df = getattr(ts, function_name)()
            result_df = result_df.to_dict('records')
            refresh_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
            return result_df, [], refresh_time

        return [], [], []

# Assign the layout to the app
app.layout = html.Div(layout)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
