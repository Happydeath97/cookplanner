# Generated by Django 4.2.2 on 2023-07-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cookplanner_app", "0011_alter_recipeingredients_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeingredients",
            name="amount",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
