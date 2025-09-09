import dash
from dash import html, register_page, dcc, callback, Output, Input, State
import requests

register_page(__name__, path="/brew", name="Brew")

# ---------- Helpers ----------
API_BASE = "https://api.openbrewerydb.org/v1/breweries"

def render_breweries(items):
    """Return a simple <ul> with brewery name, city/state, and website if available."""
    if not items:
        return html.Div("No results found.")
    lis = []
    for b in items:
        line = f"{b.get('name','(no name)')} — {b.get('city','')}, {b.get('state','')}"
        website = b.get("website_url")
        lis.append(
            html.Li([
                html.Strong(line),
                html.Span(" "),
                html.A("(website)", href=website, target="_blank") if website else None
            ])
        )
    return html.Ul(lis, className="brew-list")

# ---------- Layout ----------
layout = html.Div([
    # Top Row
    html.Div(
        html.H2("Wanna find a good drink?"),
        className="block block-top"
    ),

    # Middle: two columns
    html.Div([
        # Left column: by_city
        html.Div([
            html.H3("Find by City"),
            html.P("Type a U.S. city name to list breweries (by_city)."),
            dcc.Input(
                id="city-input",
                type="text",
                placeholder="e.g., Denver",
                debounce=True,
                className="input"
            ),
            html.Button("Search", id="btn-city", n_clicks=0, className="btn"),
            dcc.Loading(html.Div(id="city-results", className="results"))
        ], className="block"),

        # Right column: by_dist
        html.Div([
            html.H3("Sort by Distance"),
            html.P("Enter origin as latitude,longitude to sort nearest first (by_dist)."),
            dcc.Input(
                id="dist-origin",
                type="text",
                placeholder="e.g., 39.7392,-104.9903",
                debounce=True,
                className="input"
            ),
            html.Button("Find Nearby", id="btn-dist", n_clicks=0, className="btn"),
            dcc.Loading(html.Div(id="dist-results", className="results"))
        ], className="block"),
    ], className="row-2"),

    # Footer
    html.Div(
        "Data Source: Open Brewery DB is a free dataset and API with public information on breweries, cideries, brewpubs, and bottleshops.",
        className="block block-footer"
    )
], className="page2-grid")

# ---------- Callbacks ----------

# 1) Filter by city (by_city)
@callback(
    Output("city-results", "children"),
    Input("btn-city", "n_clicks"),
    State("city-input", "value"),
    prevent_initial_call=True
)
def fetch_by_city(n_clicks, city):
    if not city:
        return html.Div("Please enter a city.")
    try:
        # Simple use of by_city; limit to 10 results for readability
        r = requests.get(
            API_BASE,
            params={"by_city": city, "per_page": 10},
            timeout=8
        )
        r.raise_for_status()
        data = r.json()
        return render_breweries(data)
    except requests.RequestException as e:
        return html.Div(f"Error contacting Open Brewery DB: {e}")

# 2) Sort by distance from origin (by_dist)
@callback(
    Output("dist-results", "children"),
    Input("btn-dist", "n_clicks"),
    State("dist-origin", "value"),
    prevent_initial_call=True
)
def fetch_by_distance(n_clicks, origin):
    if not origin:
        return html.Div("Please enter an origin as latitude,longitude (e.g., 39.7392,-104.9903).")
    # Basic validation for "lat,lon"
    parts = [p.strip() for p in origin.split(",")] if isinstance(origin, str) else []
    if len(parts) != 2:
        return html.Div("Format must be latitude,longitude (e.g., 39.7392,-104.9903).")
    lat, lon = parts
    try:
        # Use by_dist to sort; include a per_page cap
        r = requests.get(
            API_BASE,
            params={"by_dist": f"{lat},{lon}", "per_page": 10},
            timeout=8
        )
        r.raise_for_status()
        data = r.json()
        return render_breweries(data)
    except requests.RequestException as e:
        return html.Div(f"Error contacting Open Brewery DB: {e}")
