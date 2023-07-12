from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.response import TemplateResponse
from users.models import User
from cookplanner_app.models import Recipe, MealPlan, Meal, RecipeIngredients
from django.contrib.auth.mixins import LoginRequiredMixin

from collections import defaultdict


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):

        return TemplateResponse(request, "index.html")


class AllRecipesView(View):

    def get(self, request, *args, **kwargs):
        context = {
            "recipes": Recipe.objects.all(),
        }
        return TemplateResponse(request, "recipes.html", context=context)


class AllMealPlansView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        mealplans = MealPlan.objects.filter(user=user)

        context = {
            "mealplans": mealplans
        }

        return TemplateResponse(request, "allmealplans.html", context=context)


class MealPlanView(LoginRequiredMixin, View):
    def get(self, request, meal_plan_id, *args, **kwargs):
        # Dictionary to store the ingredient amounts
        ingredient_amounts = defaultdict(int)
        days = {
            'Monday': {'Breakfast': None, 'Lunch': None, 'Snack': None, 'Dinner': None},
            'Tuesday': {'Breakfast': None, 'Lunch': None, 'Snack': None, 'Dinner': None},
            'Wednesday': {'Breakfast': None, 'Lunch': None, 'Snack': None, 'Dinner': None},
            'Thursday': {'Breakfast': None, 'Lunch': None, 'Snack': None, 'Dinner': None},
            'Friday': {'Breakfast': None, 'Lunch': None, 'Snack': None, 'Dinner': None},
            'Saturday': {'Breakfast': None, 'Lunch': None, 'Snack': None, 'Dinner': None},
            'Sunday': {'Breakfast': None, 'Lunch': None, 'Snack': None, 'Dinner': None}
        }

        meal_plan = MealPlan.objects.get(id=meal_plan_id)
        meals = Meal.objects.all().filter(meal_plan=meal_plan)

        for meal in meals:
            days[meal.day][meal.category] = meal
            recipe = meal.recipe

            recipe_ingredients = RecipeIngredients.objects.filter(recipe=recipe)

            for recipe_ingredient in recipe_ingredients:
                ingredient = recipe_ingredient.ingredients
                amount = recipe_ingredient.amount

                ingredient_amounts[ingredient.name] += amount

        context = {
            'meal_plan': {
                'name': meal_plan.name,
                'days': days.items(),
                'ingredient_amounts': ingredient_amounts.items()
            }
        }

        return TemplateResponse(request, "mealplan.html", context=context)


class CreateMealPlanView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}

        return TemplateResponse(request, "createmealplan.html", context=context)
