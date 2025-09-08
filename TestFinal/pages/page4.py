import dash
from dash import html

dash.register_page(__name__, path="/about", name="About")

layout = html.Div([
    html.H3("About This App"),
    html.P("Built with Dash + Food & Drink APIs."),
    html.P("APIs: Open Brewery DB, Punk API, TheMealDB (optional).")
])
