from django.contrib import admin
from .models import Ingredients, Recipe, RecipeIngredients, Taste, MealPlan, Meal, Comment

# Register your models here.


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredients
    extra = 1


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "id", "name", "prep_time",
        "cook_time", "difficulty", "description",
        "taste", "process", "rating"
    ]
    inlines = (RecipeIngredientInline,)


admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredients)
admin.site.register(Taste)
admin.site.register(MealPlan)
admin.site.register(Meal)
admin.site.register(Comment)
