from django.db import models
from django.contrib.auth.models import AbstractUser
from cookplanner_app.models import Recipe

# Create your models here.


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField()


class UserProfile(models.Model):
    favorites = models.ManyToManyField(Recipe, related_name='favorites', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"UserProfile [{self.pk}] ({self.user.username})"
