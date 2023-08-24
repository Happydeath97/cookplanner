import requests
from cookplanner_app.models import Ingredients, Recipe, RecipeIngredients, Taste
# Replace 'YOUR_APP_ID' and 'YOUR_APP_KEY' with your actual Edamam API credentials
APP_ID = 'e1b849e6'
APP_KEY = '47a6c0945ba54f5f7a2c07513f10a530'
# Base URL for the Edamam Recipe Search API
BASE_URL = 'https://api.edamam.com/search'
# Parameters for the API request
params = {
    'q': 'breakfast',
    'app_id': APP_ID,
    'app_key': APP_KEY,
    'from': 0,  # Start index of the results
    'to': 100,  # End index of the results (max 100)
    'mealType': 'dinner',  # To ensure we get breakfast recipes
}
response = requests.get(BASE_URL, params=params)
if response.status_code == 200:
    data = response.json()
    recipes = data.get('hits', [])
    neutral_taste = Taste.objects.get(name="neutral")
    for recipe in recipes:
        calorie = recipe['recipe']["calories"]
        recipe_name = recipe['recipe']['label']
        cook_time = int(recipe['recipe']['totalTime']) * 60
        print("delta time", cook_time)
        ingredients = []
        for ingredient in recipe['recipe']['ingredients']:
            ingredient_name = ingredient["food"]
            ingredient_amount = ingredient["weight"]
            if ingredient_amount == 0:
                continue
            existing = Ingredients.objects.filter(name=ingredient_name).first()
            print(".")
            if not existing:
                ingr = Ingredients(name=ingredient_name)
                ingr.save()
                existing = Ingredients.objects.filter(name=ingredient_name).first()
                ingredients.append((existing, ingredient_amount))
            else:
                ingredients.append((existing, ingredient_amount))
        rec = Recipe(name=recipe_name, cook_time=cook_time,  difficulty=2, image=None, taste=neutral_taste, calorie=calorie)
        rec.save()
        print(f"recipe saved: {recipe_name}")
        for ingredient, amount in ingredients:
            RecipeIngredients.objects.create(recipe=rec, ingredients=ingredient, amount=amount, unit="g")
else:
    print("Failed to retrieve recipes:", response.status_code)
