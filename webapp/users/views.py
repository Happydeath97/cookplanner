from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import redirect, resolve_url, render
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm


# Create your views here.


class RegisterView(View):

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
        else:
            return TemplateResponse(request, 'register.html', context={'form': form})

    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()

        context = {'form': form}

        return TemplateResponse(request, 'register.html', context)


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')
