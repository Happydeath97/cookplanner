from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import redirect, resolve_url, render
from django.contrib.auth import authenticate, login, logout
from users.models import User


# Create your views here.


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        # to be implemented

        return TemplateResponse(request, "register.html")


class LoginView(View):
    def get(self, request, *args, **kwargs):
        # to be implemented

        return TemplateResponse(request, "login.html")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')
