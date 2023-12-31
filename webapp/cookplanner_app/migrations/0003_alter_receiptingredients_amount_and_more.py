# Generated by Django 4.2.2 on 2023-06-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookplanner_app', '0002_alter_recipe_cook_time_alter_recipe_prep_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptingredients',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredients', through='cookplanner_app.ReceiptIngredients', to='cookplanner_app.ingredients'),
        ),
    ]
