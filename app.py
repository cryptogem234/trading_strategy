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
df_strategies = pd.DataFrame(columns=['strategy_name', 'eff_date', 'ticker', 'action'])
df_strategies2 = pd.DataFrame(columns=['strategy_name', 'eff_date', 'ticker', 'action'])

# Define layout
app.layout = html.Div([
    html.H1("Strategies List"),

    # Dash DataTable component for the first table
    DataTable(
        id='data-table',
        columns=[{'name': col, 'id': col} for col in df_strategies.columns],
        data=df_strategies.to_dict('records'),
    ),

    # Button for manual refresh of the first table
    html.Div([
        html.Button("Refresh Data", id='refresh-button', n_clicks=0),
        dcc.Loading(id="loading", type="circle", children=[]),
    ]),

    html.Hr(),  # Add a horizontal line for separation

    # Dash DataTable component for the second table
    DataTable(
        id='another-table',
        columns=[{'name': col, 'id': col} for col in df_strategies2.columns],
        data=df_strategies2.to_dict('records'),
    ),

    # Button for manual refresh of the second table
    html.Div([
        html.Button("Refresh Another Table", id='refresh-another-button', n_clicks=0),
        dcc.Loading(id="loading-another", type="circle", children=[]),
    ]),

])

# Define callbacks for the first table
@app.callback(
    [Output('data-table', 'data'),
     Output('loading', 'children')],
    [Input('refresh-button', 'n_clicks')],
    [State('loading', 'children')],
    prevent_initial_call=True
)
def update_output(n_clicks, children):
    if n_clicks > 0:
        result_df = ts.execute_tqqq_or_not_strategy()
        result_df = result_df.to_dict('records')
        return result_df, []

    return [], []

# Define callbacks for the second table
@app.callback(
    [Output('another-table', 'data'),
     Output('loading-another', 'children')],
    [Input('refresh-another-button', 'n_clicks')],
    [State('loading-another', 'children')],
    prevent_initial_call=True
)
def update_another_table(n_clicks, children):
    if n_clicks > 0:
        result_df = ts.execute_russell_rat_ftlt_strategy()
        result_df = result_df.to_dict('records')
        return result_df, []

    return [], []

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
