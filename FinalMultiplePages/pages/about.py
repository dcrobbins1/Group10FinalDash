#about us - daniel

import dash
from dash import html

dash.register_page(__name__, path="/about")

layout = html.Div(
    className="about-container",
    children=[
        html.H1("About Us", className="about-title"),

        html.Div(
            className="team-container",
            children=[
                # jessie
                html.Div(
                    className="team-card",
                    children=[
                        html.Img(src="Group10FinalDash/FinalMultiplePages/assets/JL.jpg", className="team-photo"),
                        html.H3("Jessie Lin", className="team-name"),
                        html.P("Jessie is an MSBA student at William & Mary's Raymond A. Mason School of Business. Jessie completed her Bachelor of Arts degree at William & Mary in 2025 where she majored in Economics and Government.", className="team-bio"),
                    ],
                ),

                # redeemer
                html.Div(
                    className="team-card",
                    children=[
                        html.Img(src="Group10FinalDash/FinalMultiplePages/assets/RG.jpg", className="team-photo"),
                        html.H3("Redeemer Gawu", className="team-name"),
                        html.P("xxx", className="team-bio"),
                    ],
                ),

                # thirtha
                html.Div(
                    className="team-card",
                    children=[
                        html.Img(src="Group10FinalDash/FinalMultiplePages/assets/TPU.jpg", className="team-photo"),
                        html.H3("Thirtha Poruthikode Unnivelan", className="team-name"),
                        html.P("Thirtha is an MSBA student at William & Mary's Raymond A. Mason School of Business. She graduated from the College of William & Mary in 2025 with a Bachelor of Arts degree in International Relations with a minor in Gender, Sexuality, & Women's Studies.", className="team-bio"),
                    ],
                ),

                # daniel
                html.Div(
                    className="team-card",
                    children=[
                        html.Img(src="Group10FinalDash/FinalMultiplePages/assets/DCR.jpg", className="team-photo"),
                        html.H3("Daniel Connor Robbins", className="team-name"),
                        html.P("Daniel is an MSBA student at William & Mary's Raymond A. Mason School of Business. Daniel completed his Bachelor of Arts degree at William & Mary in 2025 where he majored in International Relations and Global Business.", className="team-bio"),
                    ],
                ),
            ],
        ),
    ],
)
