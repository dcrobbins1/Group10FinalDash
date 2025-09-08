import dash
from dash import html

dash.register_page(__name__, path="/", name="Home")

layout = html.Div([
    html.H2("Welcome to the Food & Drinks Explorer"),
    html.P("Use the navigation above to discover breweries, beers, and recipes."),
    html.P("This dashboard uses live APIs (Open Brewery DB, Punk API, etc.) with interactive charts.")
])
