# Generated by Django 4.2.2 on 2023-08-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookplanner_app', '0016_alter_recipe_cook_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.DurationField(default=0),
        ),
    ]
