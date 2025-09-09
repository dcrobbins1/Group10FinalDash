import dash
from dash import html, dcc, register_page
import pandas as pd
import plotly.express as px
from pathlib import Path

register_page(__name__, path="/alcohol", name="Alcohol Stats")

# Load Data
DataPath = Path(__file__).resolve().parent.parent / "data" / "drinks.csv"
df = pd.read_csv(DataPath)

# Convert litres to gallons
df["total_gallons"] = df["total_litres_of_pure_alcohol"] * 0.264172

# Get top 10 countries by alcohol consumption
top10 = df.sort_values("total_gallons", ascending=False).head(10)

# Check if United States is in top 10
us_row = df[df["country"] == "USA"]
if not us_row.empty and "USA" not in top10["country"].values:
    top10 = pd.concat([top10, us_row])

# Rebuild chart with filtered data
fig = px.bar(
    top10.sort_values("total_gallons", ascending=False),
    x="country",
    y="total_gallons",
    title="Top Alcohol Consuming Countries + USA (Gallons)",
    labels={"total_gallons": "Gallons of Pure Alcohol"},
    height=600
)
# below is the code for the choropleth graph for year 2023 within US by state 

# Load Data
DataPath = Path(__file__).resolve().parent.parent / "data" / "alcohol-consumption-by-state-2025.csv"
df = pd.read_csv(DataPath)
df["total_gallons"] = df["AlcoholConsumption_EthanolConsumption_gallonsPerCapita_2023"]

# give states with state codes
state_to_abbrev = {
    "Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA","Colorado":"CO",
    "Connecticut":"CT","Delaware":"DE","District of Columbia":"DC","Florida":"FL","Georgia":"GA",
    "Hawaii":"HI","Idaho":"ID","Illinois":"IL","Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY",
    "Louisiana":"LA","Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN",
    "Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV","New Hampshire":"NH",
    "New Jersey":"NJ","New Mexico":"NM","New York":"NY","North Carolina":"NC","North Dakota":"ND",
    "Ohio":"OH","Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","Rhode Island":"RI",
    "South Carolina":"SC","South Dakota":"SD","Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT",
    "Virginia":"VA","Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY"
}

df["state"] = df["state"].astype(str).str.strip()
if df["state"].str.len().eq(2).all():
    df["state_code"] = df["state"].str.upper()
else:
    df["state_code"] = df["state"].map(state_to_abbrev)


# Choropleth 
fig = px.choropleth(
    df,
    locations="state_code",
    locationmode="USA-states",
    color="total_gallons",
    scope="usa",
    hover_data={"state": True, "total_gallons": ":.2f", "state_code": False},
    title="Per Capita Alcohol Consumption by State, 2023",
    color_continuous_scale="blues",
    height=600,
    labels={"total_gallons": "Gallons of Alcohol Consumed"}
)
fig.update_layout(
    margin=dict(l=0, r=0, t=60, b=0),
    title={'text': "Per Capita Alcohol Consumption by State, 2023", 'x': 0.5}
)

# Layout
layout = html.Div([
    html.H2("Alcohol Consumption Around the World", className="heading"),

    html.P(
        "This chart shows the top 10 countries by average annual alcohol consumption per person, plus the United States, converted to gallons.",
        className="info-paragraph"
    ),

    dcc.Graph(figure=fig),
    html.Div([
    html.H2("Alcohol Consumption Within the US", className="heading", style={'textAlign': 'center'}),

    html.P(
        "This choropleth chart shows the average annual alcohol consumption per person by state (2023).",
        className="info-paragraph"
    ),

    dcc.Graph(figure=fig),

    html.A("Back to Home", href="/", className="nav-link"),

    html.Div("Source: FiveThirtyEight / WHO", className="source-note"),
    html.Div("Source: World Population Review", className="source-note")
], className="page-container")
