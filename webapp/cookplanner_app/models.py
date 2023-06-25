from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Ingredients(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Recipe(models.Model):
    # testing values of taste
    TASTE_SALTY = "slt"
    TASTE_SWEET = "swt"
    TASTE_SPICY = "spc"

    TASTE_CHOICES = (
        (TASTE_SALTY, "salty"),
        (TASTE_SWEET, "sweet"),
        (TASTE_SPICY, "spicy")
    )

    name = models.CharField(max_length=50)
    prep_time = models.IntegerField(validators=[MinValueValidator(1)])
    cook_time = models.IntegerField(validators=[MinValueValidator(1)])
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    description = models.TextField(blank=True)
    taste = models.CharField(choices=TASTE_CHOICES, max_length=30)
    url_recipe = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)
    ingredients = models.ManyToManyField(Ingredients, through='ReceiptIngredients', related_name='ingredients')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class ReceiptIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.PROTECT)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.ingredients.name} -> {self.recipe.name} {self.amount}g"

    def __repr__(self):
        return f"{self.ingredients.name} -> {self.recipe.name} {self.amount}g"
