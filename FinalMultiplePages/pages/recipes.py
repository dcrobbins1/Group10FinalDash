import dash
from dash import html, dcc, Input, Output, State, callback
import plotly.express as px
import pandas as pd

dash.register_page(__name__,path="/recipes", name="recipes")

# import your helper functions
from data.spoonacular_api import get_recipes_by_ingredient, get_nutrition

layout = html.Div([
    html.H2("Recipe Finder"),
    dcc.Input(id="ingredient-input", type="text", placeholder="Enter a main ingredient"),
    html.Button("Search", id="search-button"),
    html.Div(id="recipe-results"),
    html.Div(id="nutrition-chart")
])

# -------------------------
# Callback 1: Search recipes
# -------------------------
@callback(
    Output("recipe-results", "children"),
    Input("search-button", "n_clicks"),
    State("ingredient-input", "value")
)
def search_recipes(n_clicks, ingredient):
    if not n_clicks:
        return "Enter an ingredient to search."
    if not ingredient:
        return "Please type at least one ingredient."

    data = get_recipes_by_ingredient(ingredient)

    if not data:
        return "No recipes found."

    results = []
    for recipe in data:
        recipe_id = recipe["id"]
        results.append(html.Div([
            html.H4(recipe["title"]),
            html.Img(src=recipe["image"], style={"width": "200px"}),
            html.Button("Show Nutrition", id={"type": "nutrition-button", "index": recipe_id})
        ], style={"marginBottom": "20px"}))

    return results


# -------------------------
# Callback 2: Show nutrition chart
# -------------------------
@callback(
    Output("nutrition-chart", "children"),
    Input({"type": "nutrition-button", "index": str}, "n_clicks"),
    prevent_initial_call=True
)
def show_nutrition(n_clicks, recipe_id):
    if not n_clicks:
        return None

    data = get_nutrition(recipe_id)

    if "bad" not in data and "good" not in data:
        return "No nutrition data available."

    nutrients = data.get("bad", []) + data.get("good", [])
    df = pd.DataFrame(nutrients)

    fig = px.bar(
        df,
        x="title",
        y="amount",
        title="Nutrition Facts",
        labels={"title": "Nutrient", "amount": "Amount"}
    )

    return dcc.Graph(figure=fig)