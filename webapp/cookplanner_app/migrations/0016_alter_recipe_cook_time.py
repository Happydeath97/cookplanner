# Generated by Django 4.2.2 on 2023-08-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookplanner_app', '0015_recipe_calorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.DurationField(default=0),
        ),
    ]