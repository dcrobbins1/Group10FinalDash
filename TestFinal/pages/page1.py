import dash
from dash import html, dcc, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import pandas as pd, requests
import plotly.express as px

dash.register_page(__name__, path="/discover", name="Discover")

layout = dbc.Container([
    html.H3("Discover Breweries or Beers"),
    dbc.Row([
        dbc.Col(dcc.Dropdown(
            id="provider1",
            options=[{"label":"Open Brewery DB","value":"brewery"},
                     {"label":"Punk API (Beers)","value":"beer"}],
            value="brewery", clearable=False), md=4),
        dbc.Col(dbc.Input(id="query1", type="text", placeholder="Search by name..."), md=5),
        dbc.Col(dbc.Button("Search", id="search_btn1", color="primary"), md=3)
    ]),
    html.Div(id="msg1", className="mt-2"),
    dbc.Row([
        dbc.Col(dash_table.DataTable(id="results1", page_size=8, row_selectable="single"), md=7),
        dbc.Col(html.Div(id="details1"), md=5),
    ], className="mt-3"),
    dcc.Graph(id="viz1")
], fluid=True)

# Callbacks
def fetch_breweries(q):
    url = f"https://api.openbrewerydb.org/v1/breweries/search?query={q}&per_page=20"
    r = requests.get(url).json()
    return pd.DataFrame(r)

def fetch_beers(q):
    url = f"https://api.punkapi.com/v2/beers?beer_name={q}&per_page=20"
    r = requests.get(url).json()
    return pd.json_normalize(r)

@dash.callback(
    Output("results1","data"), Output("results1","columns"), Output("msg1","children"),
    Input("search_btn1","n_clicks"), State("provider1","value"), State("query1","value"),
    prevent_initial_call=True
)
def search(_, provider, q):
    if provider=="brewery":
        df = fetch_breweries(q or "dog")
        cols = ["name","brewery_type","city","state"]
        return df[cols].to_dict("records"), [{"name":c,"id":c} for c in cols], f"Found {len(df)} breweries."
    else:
        df = fetch_beers(q or "ale")
        cols = ["name","abv","ibu","first_brewed"]
        return df[cols].to_dict("records"), [{"name":c,"id":c} for c in cols], f"Found {len(df)} beers."