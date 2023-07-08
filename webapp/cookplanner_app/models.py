from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Ingredients(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Taste(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    name = models.CharField(max_length=50)
    prep_time = models.IntegerField(validators=[MinValueValidator(1)])
    cook_time = models.IntegerField(validators=[MinValueValidator(1)])
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    description = models.TextField(blank=True)
    taste = models.ForeignKey(Taste, on_delete=models.PROTECT, related_name='taste')
    url_recipe = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)
    ingredients = models.ManyToManyField(Ingredients, through='RecipeIngredients', related_name='ingredients')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.PROTECT)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.ingredients.name} -> {self.recipe.name} {self.amount}g"

    def __repr__(self):
        return f"{self.ingredients.name} -> {self.recipe.name} {self.amount}g"
