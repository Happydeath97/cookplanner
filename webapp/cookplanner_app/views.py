from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.response import TemplateResponse
from users.models import User
from cookplanner_app.models import Recipe, MealPlan, Meal
from django.contrib.auth.mixins import LoginRequiredMixin


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
    def get(self, request, *args, **kwargs):
        context = {}

        return TemplateResponse(request, "mealplan.html", context=context)


class CreateMealPlanView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}

        return TemplateResponse(request, "createmealplan.html", context=context)
