# home page

import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div([
    html.H2("Welcome to our Home Page"),
    html.P("We will add more info later")
    
])