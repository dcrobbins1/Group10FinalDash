import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Initialize app with pages support
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

#app.layout = dbc.Container([
#    html.H1("Food & Drinks Explorer", className="text-center my-3"),
#    dbc.Nav(
##            dbc.NavLink("Home", href="/", active="exact"),
  #          dbc.NavLink("About", href="/about",active="exact"),
  #          dbc.NavLink("Recipes", href="/recipes",active="exact"),
  #          dbc.NavLink("Brewery", href="/brew",active="exact"),
   #         for page in dash.page_registry.values()
   #     ],
   #     pills=True,
   #     justified=True,
    #    className="mb-4"
    #),
 #   dash.page_container
#], fluid=True)

app.layout = dbc.Container([
    html.H1("Food & Drinks Explorer", className="text-center my-3"),
    dbc.Nav(
        [
            dbc.NavLink("Home", href="/", active="exact"),
            dbc.NavLink("Recipes", href="/recipes",active="exact"),
            dbc.NavLink("Brewery", href="/brew",active="exact"),
            dbc.NavLink("Alcohol Warnings", href="/alcohol",active="exact"),
            dbc.NavLink("About Us", href="/about",active="exact"),
        ],
        pills=True,
        justified=True,
        className="mb-4"
    ),
    dash.page_container
], fluid=True)



if __name__ == "__main__":

    app.run(debug=True)


