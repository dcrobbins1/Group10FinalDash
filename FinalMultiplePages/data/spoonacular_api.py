import requests

API_KEY = "67a21770bc7b4e30bedd7ceba76dedd0"

def get_recipes_by_ingredient(ingredient, n=5):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredient}&number={n}&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_nutrition(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json?apiKey={API_KEY}"
    response = requests.get(url)
    return response.json()