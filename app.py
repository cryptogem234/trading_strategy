import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash_table import DataTable
import pandas as pd
import total_strategies as ts
from datetime import datetime
import pytz

# Create Dash app
app = dash.Dash(__name__)
server = app.server

# Initialize dataframes
col_list = ['strategy_name','date','ticker','close','pctreturn','pct_alloc']
tqqq_or_not = pd.DataFrame(columns=col_list)
rat_ftlt = pd.DataFrame(columns=col_list)
nothing_but_bonds = pd.DataFrame(columns=col_list)
short_volatility_svxy = pd.DataFrame(columns=col_list)
short_volatility = pd.DataFrame(columns=col_list)
beta_baller = pd.DataFrame(columns=col_list)
wam_ftlt = pd.DataFrame(columns=col_list)
holy_grail = pd.DataFrame(columns=col_list)
bnd_20d_sh_60d = pd.DataFrame(columns=col_list)
medium_time_frame_switches = pd.DataFrame(columns=col_list)
wmdyn_ftlt = pd.DataFrame(columns=col_list)
anansi_strategy = pd.DataFrame(columns=col_list)


# Define a list of dictionaries for each table
tables = [
    {'id': 'beta_baller', 'df': beta_baller, 'button_id': 'refresh-button1', 'name': '1. Beta Baller'},
    {'id': 'short_volatility', 'df': short_volatility, 'button_id': 'refresh-button2', 'name': '2. Short Volatility'},
    {'id': 'wam_ftlt', 'df': wam_ftlt, 'button_id': 'refresh-button3', 'name': '3. WAM FTLT'},
    {'id': 'holy_grail', 'df': holy_grail, 'button_id': 'refresh-button4', 'name': '4. Holy Grail'},
    {'id': 'bnd_20d_sh_60d', 'df': bnd_20d_sh_60d, 'button_id': 'refresh-button5', 'name': '5. Simple 20d BND vs 60d SH'},
    {'id': 'wmdyn_ftlt', 'df': wmdyn_ftlt, 'button_id': 'refresh-button6', 'name': '6. WMDYN FTLT'},

    {'id': 'tqqq_or_not', 'df': tqqq_or_not, 'button_id': 'refresh-button7', 'name': '1. TQQQ or Not'},
    {'id': 'short_volatility_svxy', 'df': short_volatility_svxy, 'button_id': 'refresh-button8', 'name': '2. Short Volatility SVXY'},
    {'id': 'rat_ftlt', 'df': rat_ftlt, 'button_id': 'refresh-button9', 'name': '3. RAT FTLT'},
    {'id': 'nothing_but_bonds', 'df': nothing_but_bonds, 'button_id': 'refresh-button10', 'name': '4. Nothing but Bonds'},
    {'id': 'medium_time_frame_switches', 'df': medium_time_frame_switches, 'button_id': 'refresh-button11', 'name': '5. Medium Time Frame Switches'},
    {'id': 'anansi_strategy', 'df': anansi_strategy, 'button_id': 'refresh-button12', 'name': '6. Anansi Portfolio'},
]

# Define layout dynamically
layout = [html.H1("Strategies List")]

# Add Dash DataTable components for each table dynamically
for idx, table in enumerate(tables):
    layout.extend([
        html.H3(table['name'], style={'font-size': '1.2rem', 'margin-bottom': '0'}),
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

    # Insert sub-heading after Table 5
    if idx == 5:
        layout.append(html.H2("-----Model Portfolios-------"))

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

            # Convert the current UTC time to EST
            est = pytz.timezone('US/Eastern')
            refresh_time_utc = datetime.now()
            refresh_time_est = refresh_time_utc.astimezone(est)
            refresh_time = refresh_time_est.strftime("%Y-%m-%d %I:%M:%S %p")

            return result_df, [], refresh_time

        return [], [], []

# Assign the layout to the app
app.layout = html.Div(layout)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
