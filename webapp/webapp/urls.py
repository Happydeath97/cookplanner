"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cookplanner_app.views import IndexView, AllRecipesView, AllMealPlansView, MealPlanView, CreateMealPlanView, RecipeView, EditMealPlanView
from users.views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("recipes/", AllRecipesView.as_view(), name="all_recipes"),
    path("recipe/<int:recipe_id>/", RecipeView.as_view(), name="recipe"),
    path("mealplans/", AllMealPlansView.as_view(), name="all_mealplans"),
    path("mealplan/<int:meal_plan_id>/", MealPlanView.as_view(), name="mealplan"),
    path("createmealplan/", CreateMealPlanView.as_view(), name="create_mealplan"),
    path("editmealplan/<int:meal_plan_id>/", EditMealPlanView.as_view(), name="edit_mealplan"),
]
