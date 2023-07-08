from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.response import TemplateResponse
from cookplanner_app.models import Recipe


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

