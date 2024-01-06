import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash_table import DataTable
import pandas as pd
import total_strategies as ts

# Create Dash app
app = dash.Dash(__name__)
server = app.server

# Initialize dataframes
tqqq_or_not = pd.DataFrame(columns=['strategy_name', 'eff_date', 'ticker'])
russell_rat_ftlt = pd.DataFrame(columns=['strategy_name', 'eff_date', 'ticker'])
nothing_but_bonds = pd.DataFrame(columns=['strategy_name', 'eff_date', 'ticker'])
short_volatility_svxy = pd.DataFrame(columns=['strategy_name', 'eff_date', 'ticker'])

# Define a list of dictionaries for each table
tables = [
    {'id': 'tqqq_or_not', 'df': tqqq_or_not, 'button_id': 'refresh-button'},
    {'id': 'russell_rat_ftlt', 'df': russell_rat_ftlt, 'button_id': 'refresh-button2'},
    {'id': 'nothing_but_bonds', 'df': nothing_but_bonds, 'button_id': 'refresh-button3'},
    {'id': 'short_volatility_svxy', 'df': nothing_but_bonds, 'button_id': 'refresh-button4'}
]

# Define layout dynamically
layout = [html.H1("Strategies List")]

# Add Dash DataTable components for each table dynamically
for table in tables:
    layout.extend([
        DataTable(
            id=table['id'],
            columns=[{'name': col, 'id': col} for col in table['df'].columns],
            data=table['df'].to_dict('records'),
            style_cell={'minWidth': '100px', 'maxWidth': '100px', 'textAlign': 'left'},
        ),
        html.Div([
            html.Button("Refresh Data", id=table['button_id'], n_clicks=0),
            dcc.Loading(id=f"loading-{table['id']}", type="circle", children=[]),
        ]),
        html.Hr()  # Add a horizontal line for separation after each table
    ])

# Define callbacks dynamically
for table in tables:
    @app.callback(
        [Output(table['id'], 'data'),
         Output(f"loading-{table['id']}", 'children')],
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
            return result_df, []

        return [], []

# Assign the layout to the app
app.layout = html.Div(layout)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
