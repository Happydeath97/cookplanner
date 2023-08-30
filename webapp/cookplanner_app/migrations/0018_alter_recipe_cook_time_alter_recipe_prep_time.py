# Generated by Django 4.2.2 on 2023-08-21 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookplanner_app', '0017_alter_recipe_prep_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.PositiveIntegerField(default=0),
        ),
    ]