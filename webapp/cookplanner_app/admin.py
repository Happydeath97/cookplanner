from django.contrib import admin
from .models import Ingredients, Recipe, ReceiptIngredients

# Register your models here.


class RecipeIngredientInline(admin.TabularInline):
    model = ReceiptIngredients
    extra = 1


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "id", "name", "prep_time",
        "cook_time", "difficulty", "description",
        "taste", "url_recipe", "rating"
    ]
    inlines = (RecipeIngredientInline,)


admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(ReceiptIngredients)
