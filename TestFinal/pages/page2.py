import dash
from dash import html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd, requests

dash.register_page(__name__, path="/analyze", name="Analyze")

layout = html.Div([
    html.H3("Analyze Breweries/Beers"),
    dcc.Dropdown(id="provider2", options=[
        {"label":"Open Brewery DB","value":"brewery"},
        {"label":"Punk API (Beers)","value":"beer"}],
        value="brewery", clearable=False),
    dcc.Input(id="param2", type="text", placeholder="State for breweries or max ABV for beers"),
    html.Button("Analyze", id="btn2"),
    dcc.Graph(id="viz2a"), dcc.Graph(id="viz2b")
])

@dash.callback(
    Output("viz2a","figure"), Output("viz2b","figure"),
    Input("btn2","n_clicks"), State("provider2","value"), State("param2","value"),
    prevent_initial_call=True
)
def analyze(_, provider, param):
    if provider=="brewery":
        url = f"https://api.openbrewerydb.org/v1/breweries?by_state={param or 'California'}&per_page=50"
        df = pd.DataFrame(requests.get(url).json())
        return px.pie(df, names="brewery_type", title="Types"), px.bar(df["city"].value_counts().head(10))
    else:
        url = f"https://api.punkapi.com/v2/beers?abv_lt={param or 8}&per_page=50"
        df = pd.json_normalize(requests.get(url).json())
        return px.histogram(df, x="abv"), px.bar(df["first_brewed"].value_counts().head(10))