# Generated by Django 4.2.3 on 2023-07-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookplanner_app', '0007_rename_title_mealplan_name_alter_meal_meal_plan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredients',
            name='unit',
            field=models.CharField(default='g', max_length=10),
        ),
        migrations.AlterField(
            model_name='recipeingredients',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
