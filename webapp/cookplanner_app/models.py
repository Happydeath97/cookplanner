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
    prep_time = models.DurationField()
    cook_time = models.DurationField()
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
    amount = models.PositiveIntegerField()
    unit = models.CharField(default='g', max_length=10)

    def __str__(self):
        return f"{self.ingredients.name} -> {self.recipe.name} {self.amount}g"

    def __repr__(self):
        return f"{self.ingredients.name} -> {self.recipe.name} {self.amount}g"


class MealPlan(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} {self.name}"

class Meal(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    CATEGORY_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]

    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name='meal_plan')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe')
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"User: {self.meal_plan.user.username} Meal plan: {self.meal_plan} " \
               f"Meal: {self.recipe.name} - {self.day} {self.category}"
