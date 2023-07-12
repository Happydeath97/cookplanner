# Generated by Django 4.2.3 on 2023-07-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookplanner_app', '0007_rename_title_mealplan_name_alter_meal_meal_plan_and_more'),
        ('users', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='cookplanner_app.recipe'),
        ),
    ]