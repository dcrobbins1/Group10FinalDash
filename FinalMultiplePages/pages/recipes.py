# recipe.py  (Recipe page for your multipage Dash app)
import dash
from dash import html,register_page, dcc, callback, Output, Input
import requests
# (added) extra import needed for reading input values when a button is clicked
from dash import State

# Register this page
register_page(__name__, path="/recipes", name="Recipe")

API_BASE = "https://www.themealdb.com/api/json/v1/1"  

def _ingredientize(s: str) -> str:
    """Turn user text into TheMealDB ingredient format (spaces -> underscores)."""
    if not s:
        return ""
    return s.strip().lower().replace(" ", "_")

def _render_meal_details(meal: dict):
    """Create a simple recipe card with image, ingredients list, and instructions."""
    if not meal:
        return html.Div("No recipe details found.")

    # Collect ingredients 
    ing_items = []
    for i in range(1, 21):
        ing = (meal.get(f"strIngredient{i}") or "").strip()
        mea = (meal.get(f"strMeasure{i}") or "").strip()
        if ing:
            ing_items.append(html.Li(f"{mea} {ing}".strip()))

    # Main bits
    title = meal.get("strMeal", "(no name)")
    area = meal.get("strArea") or ""
    category = meal.get("strCategory") or ""
    img = meal.get("strMealThumb")
    yt = meal.get("strYoutube")

    return html.Div([
        html.H4(title),
        html.P(f"{category} {f'— {area}' if area else ''}"),
        html.Img(src=img, alt=title, style={"maxWidth": "320px"}) if img else None,
        html.H5("Ingredients"),
        html.Ul(ing_items) if ing_items else html.Div("No ingredients listed."),
        html.H5("Instructions"),
        html.P(meal.get("strInstructions") or "No instructions provided."),
        html.Div(
            html.A("Watch on YouTube", href=yt, target="_blank"),
            style={"marginTop": "8px"}
        ) if yt else None
    ], className="recipe-card")

# ---------------- Layout ----------------
layout = html.Div([
    # Top Row
    html.Div(
        html.H2("Wanna find a delicious recipe?"),
        className="block block-top"
    ),

    # Middle (single column)
    html.Div([
        html.H3("Filter by main ingredient"),
        html.P("Type an ingredient and click Search (e.g., chicken_breast or chicken breast)."),
        dcc.Input(
            id="ingredient-input",
            type="text",
            placeholder="e.g., chicken_breast",
            debounce=True,
            className="input"
        ),
        html.Button("Search", id="btn-ingredient", n_clicks=0, className="btn"),

        # Status message for search + the dropdown of meals
        dcc.Loading(html.Div(id="search-msg", className="results-msg")),
        dcc.Dropdown(
            id="meal-select",
            options=[],      # will be filled by callback #1
            value=None,
            placeholder="Select a meal from results...",
            clearable=True,
            className="dropdown"
        ),

        # Where recipe details will be shown
        dcc.Loading(html.Div(id="meal-details", className="results"))
    ], className="block"),

    # Footer
    html.Div(
        "Data Source: TheMealDB: An open, crowd-sourced database of recipes from around the world. We offer a free recipe API for anyone wanting to use it, with additional premium features if required..",
        className="block block-footer"
    )
], className="recipe-grid")

# ---------------- Callbacks ----------------

# 1) Filter by main ingredient -> populate dropdown (and show a small status)
@callback(
    Output("meal-select", "options"),
    Output("search-msg", "children"),
    Input("btn-ingredient", "n_clicks"),
    State("ingredient-input", "value"),
    prevent_initial_call=True
)
def filter_by_ingredient(n_clicks, ingredient_text):
    ing = _ingredientize(ingredient_text)
    if not ing:
        return [], html.Div("Please enter a main ingredient.")

    try:
        r = requests.get(f"{API_BASE}/filter.php", params={"i": ing}, timeout=8)
        r.raise_for_status()
        data = r.json() or {}
        meals = data.get("meals")
        if not meals:
            return [], html.Div(f"No meals found for ingredient: {ing}")
        options = [{"label": m.get("strMeal", f"Meal {m.get('idMeal')}"),
                    "value": m.get("idMeal")} for m in meals]
        return options, html.Div(f"Found {len(options)} meals. Pick one to see the recipe.")
    except requests.RequestException as e:
        return [], html.Div(f"Error contacting TheMealDB: {e}")

# 2) Select a meal -> show detailed recipe card
@callback(
    Output("meal-details", "children"),
    Input("meal-select", "value"),
    prevent_initial_call=True
)
def show_meal_details(meal_id):
    if not meal_id:
        return html.Div("Select a meal to see details.")
    try:
        r = requests.get(f"{API_BASE}/lookup.php", params={"i": meal_id}, timeout=8)
        r.raise_for_status()
        data = r.json() or {}
        meals = data.get("meals") or []
        meal = meals[0] if meals else {}
        return _render_meal_details(meal)
    except requests.RequestException as e:
        return html.Div(f"Error contacting TheMealDB: {e}")
