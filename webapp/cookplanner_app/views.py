from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseForbidden
from django.template.response import TemplateResponse
from users.models import User
from cookplanner_app.models import Recipe, MealPlan, Meal, RecipeIngredients
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from collections import defaultdict
from cookplanner_app.forms import RecipeForm

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


class RecipeView(View):

    def get(self, request, recipe_id, *args, **kwargs):
        recipe = Recipe.objects.get(id=recipe_id)
        context = {
            'recipe': recipe
        }

        return TemplateResponse(request, "recipe.html", context=context)


class CreateRecipeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = RecipeForm()

        return TemplateResponse(request, "create_recipe.html", context={"form": form})
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            recipe = form.save()
        else:
            print(form.errors)


        context = {
            'form': form
        }

        return TemplateResponse(request, "recipe.html", context=context)


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

        ingredient_amounts = defaultdict(int)
        ingredient_units = {}
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
        meals = meal_plan.meal_plan.all()  # Meal.objects.all().filter(meal_plan=meal_plan)

        for meal in meals:
            days[meal.day][meal.category] = meal
            recipe = meal.recipe

            recipe_ingredients = RecipeIngredients.objects.filter(recipe=recipe)

            for recipe_ingredient in recipe_ingredients:
                ingredient = recipe_ingredient.ingredients
                amount = recipe_ingredient.amount
                unit = recipe_ingredient.unit

                ingredient_amounts[(ingredient.name, unit)] += amount
                ingredient_units[(ingredient.name, unit)] = unit

        result = [{'ingredient': ingredient, 'amount': amount, 'unit': unit} for (ingredient, unit), amount in
                  ingredient_amounts.items()]

        context = {
            'meal_plan': {
                'name': meal_plan.name,
                'days': days.items(),
                'ingredient_amounts': result
            }
        }

        return TemplateResponse(request, "mealplan.html", context=context)


class CreateMealPlanView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        return TemplateResponse(request, "createmealplan.html")

    def post(self, request, *args, **kwargs):
        user = request.user
        name = request.POST.get('name')
        if name:
            # validate form and create mealplan
            meal_plan = MealPlan(user=user, name=name)
            meal_plan.save()

            return redirect("edit_mealplan", meal_plan_id=meal_plan.id)
        else:
            messages.error(request, 'Please provide a name')
            return TemplateResponse(request, "createmealplan.html")


class EditMealPlanView(LoginRequiredMixin, View):
    def get(self, request, meal_plan_id, *args, **kwargs):
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
        meals = meal_plan.meal_plan.all()  # Meal.objects.all().filter(meal_plan=meal_plan)

        for meal in meals:
            days[meal.day][meal.category] = meal

        context = {
            "mealplan": meal_plan,
            "days": days.items(),
            "recipes": Recipe.objects.all()
        }

        return TemplateResponse(request, "editmealplan.html", context=context)

    def post(self, request, meal_plan_id, *args, **kwargs):
        recipe_id = request.POST.get('recipe')
        day = request.POST.get('day')
        category = request.POST.get('category')

        if recipe_id and day and category:
            meal_plan = MealPlan.objects.get(id=meal_plan_id)
            recipe = Recipe.objects.get(id=recipe_id)

            # Delete existing meal with the same day and category
            Meal.objects.filter(meal_plan=meal_plan, day=day, category=category).delete()

            meal = Meal(meal_plan=meal_plan, recipe=recipe, day=day, category=category)
            meal.save()

        return redirect("edit_mealplan", meal_plan_id=meal_plan_id)
