import dash
from dash import html, dcc, Input, Output, State, dash_table
import pandas as pd, requests, plotly.express as px

dash.register_page(__name__, path="/build", name="Build-Your-Own")

layout = html.Div([
    html.H3("Build Filters"),
    dcc.Dropdown(id="provider3", options=[
        {"label":"Open Brewery DB","value":"brewery"},
        {"label":"Punk API","value":"beer"}], value="beer"),
    dcc.Input(id="name3", type="text", placeholder="Name contains..."),
    dcc.Slider(id="abv3", min=3, max=15, step=0.5, value=7.5),
    html.Button("Find", id="btn3"),
    html.Div(id="msg3"),
    dash_table.DataTable(id="tbl3"),
    dcc.Graph(id="viz3")
])

@dash.callback(
    Output("tbl3","data"), Output("tbl3","columns"), Output("viz3","figure"), Output("msg3","children"),
    Input("btn3","n_clicks"), State("provider3","value"), State("name3","value"), State("abv3","value"),
    prevent_initial_call=True
)
def build(_, provider, name, abv):
    if provider=="brewery":
        url = f"https://api.openbrewerydb.org/v1/breweries/search?query={name or ''}&per_page=30"
        df = pd.DataFrame(requests.get(url).json())
        cols = ["name","brewery_type","city"]
        return df[cols].to_dict("records"), [{"name":c,"id":c} for c in cols], px.bar(df["brewery_type"].value_counts()), f"{len(df)} matches."
    else:
        url = f"https://api.punkapi.com/v2/beers?beer_name={name or ''}&abv_lt={abv}&per_page=30"
        df = pd.json_normalize(requests.get(url).json())
        cols = ["name","abv","ibu","first_brewed"]
        return df[cols].to_dict("records"), [{"name":c,"id":c} for c in cols], px.histogram(df, x="ibu"), f"{len(df)} matches."