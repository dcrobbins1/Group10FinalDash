# Food & Drinks Explorer

## Project Overview
This project is a multi-page Dash web app that helps users explore food and drink options interactively.  
- **Problem**: People often want inspiration for meals with ingredients they already have at home, or they want to discover local breweries in their city. However, finding this information usually requires searching multiple websites.  
- **Audience**: Everyday cooks, food enthusiasts, and anyone interested in exploring nearby breweries.  
- **Value**: The app combines recipe suggestions and brewery search in one convenient, user-friendly interface. It reduces time spent searching, helps reduce food waste by using existing ingredients, and connects users with local breweries.

The app has three sections:
1. **Home Page** – Overview and navigation.  
2. **Recipes Page** – Input an ingredient to see a list of recipes.
3. **Breweries Page** – Enter a city to view breweries nearby, along with interactive visualizations.

## How to Run

You can access the live app here: [Food & Drinks Exploreer]()

### Using the Live App
1. Open the link above in any web browser.  
2. Navigate through the app using the tabs:
   - **Home** – Overview of the app.
   - **Recipes** – Search for recipes by ingredient.
   - **Brewery** – Find breweries by city or distance.
   - **Alcohol Statistics** - Discover alcohol statistics across countries and states
   - **About Us** - Learn about the developers
3. Enter input values (e.g., ingredient or city) and interact with the app! Results will update dynamically.

### Running Locally (Optional)
If you want to run the app locally:
1. Clone the Github repository [Github Repo](https://github.com/dcrobbins1/Group10FinalDash.git)
2. Open VSCode and Ctrl Shift P -> click Git Clone and input link
3. Run program

## Data Sources & Data Dictionary

### 1. Recipes Data

- **Source:** [TheMealDB API](https://www.themealdb.com/api.php)  
- **API Endpoints used:**  
  - `/filter.php?i=<ingredient>` — Returns a list of recipes containing the ingredient.  
  - `/lookup.php?i=<meal_id>` — Returns detailed information for a specific recipe.  

- **Returned Data Fields:**

| Field | Description |
|-------|-------------|
| `idMeal` | Unique ID for the recipe |
| `strMeal` | Name of the recipe |
| `strMealThumb` | URL of the recipe image |
| `strCategory` | Category of the meal (e.g., Dessert, Seafood) |
| `strArea` | Cuisine origin (e.g., Italian, Mexican) |
| `strInstructions` | Step-by-step cooking instructions |
| `strYoutube` | Optional YouTube link for recipe video |
| `strIngredient1`–`strIngredient20` | Ingredients used in the recipe |
| `strMeasure1`–`strMeasure20` | Amounts for each ingredient |

---

### 2. Brewery Data

- **Source:** [Open Brewery DB API](https://www.openbrewerydb.org/)  
- **API Endpoints used:**  
  - `/breweries?by_city=<city>` — Returns breweries in a specific city.  
  - `/breweries?by_dist=<latitude,longitude>` — Returns breweries sorted by distance.  

- **Returned Data Fields:**

| Field | Description |
|-------|-------------|
| `id` | Unique ID of the brewery |
| `name` | Brewery name |
| `city` | City where brewery is located |
| `state` | State where brewery is located |
| `website_url` | URL of the brewery website (if available) |
| `brewery_type` | Type of brewery (e.g., micro, brewpub, planning) |
| `latitude` | Latitude of brewery location |
| `longitude` | Longitude of brewery location |

### 3. Alcohol Data
- **Source:** (https://github.com/datasets/five-thirty-eight-datasets/blob/main/datasets/alcohol-consumption/data/drinks.csv?plain=1)

## AI Statement:
Generative AI (ChatGPT) was used to assist with:
- Brainstorming the overall structure and layout of the multi-page Dash app
- Writing callbacks for recipe search and brewery search functionality
- Designing helper functions to fetch and process API data
- Formatting page layouts and styling with Dash/Bootstrap components
- Troubleshooting coding issues
- Improve layout on README.md

All code was reviewed, tested, and modified by the team to ensure correctness and understanding.
