# home page

import dash
from dash import html

dash.register_page(__name__, path="/", name="Home")

layout = html.Div([
    html.H2("Welcome to the Food & Drinks Explorer"),
    html.P([
    "Are you looking for a New Recipe?",
    html.Br(),
    "Are you Thirsty?",
    html.Br(),
    "You have come to the Right Place!.",
]),
html.P("Use the navigation above to Explore!."),
    
])
