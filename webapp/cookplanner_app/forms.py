from django import forms
from .models import Recipe, Taste, Ingredients, Comment


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['validation']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["stars", "text"]
