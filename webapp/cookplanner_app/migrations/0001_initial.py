# Generated by Django 4.2.2 on 2023-06-24 14:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=10)),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cookplanner_app.ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prep_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('cook_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('difficulty', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('description', models.TextField(blank=True)),
                ('taste', models.CharField(choices=[('slt', 'salty'), ('swt', 'sweet'), ('spc', 'spicy')], max_length=30)),
                ('url_recipe', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('rating', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('ingredients', models.ManyToManyField(through='cookplanner_app.ReceiptIngredients', to='cookplanner_app.ingredients')),
            ],
        ),
        migrations.AddField(
            model_name='receiptingredients',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cookplanner_app.recipe'),
        ),
    ]