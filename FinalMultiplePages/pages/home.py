# home page

import dash
from dash import html

dash.register_page(__name__, path="/", name="Home")

layout = html.Div(
    [
        html.H2("Welcome to FOOD & DRINKS EXPLORER"),
        html.P("Are you looking for a New Recipe?"),
        html.P("Are you Thirsty?"),
        html.P("You have come to the Right Place!"),
        html.P("Use the navigation above to Explore."),
    ],
    id="home"  
)

