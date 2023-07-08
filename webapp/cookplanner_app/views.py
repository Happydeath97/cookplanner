from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.response import TemplateResponse
from users.models import User


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):

        return TemplateResponse(request, "index.html")
