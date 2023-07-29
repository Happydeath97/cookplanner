from django import forms
from .models import Recipe, Taste, Ingredients


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['validation']

