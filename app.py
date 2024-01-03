import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash_table import DataTable
import pandas as pd
import total_strategies as ts

# Create Dash app
app = dash.Dash(__name__)
server = app.server

df = pd.DataFrame(columns=['strategy_name', 'eff_date', 'ticker', 'action'])

# Define layout
app.layout = html.Div([
    html.H1("Strategies List"),

    # Dash DataTable component
    DataTable(
        id='data-table',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
    ),

    # Button for manual refresh
    html.Div([
        html.Button("Refresh Data", id='refresh-button', n_clicks=0),
        dcc.Loading(id="loading", type="circle", children=[]),
    ]),

])

# Define callback
@app.callback(
    [Output('data-table', 'data'),
     Output('loading', 'children')],
    [Input('refresh-button', 'n_clicks')],
    [State('loading', 'children')],
    prevent_initial_call=True
)
def update_output(n_clicks, children):
    if n_clicks > 0:
        result_df = ts.execute_all_strategies()
        result_df = result_df.to_dict('records')
        return result_df, []

    return [], []

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
