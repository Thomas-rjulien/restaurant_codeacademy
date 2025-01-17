# Generated by Django 5.0.6 on 2024-07-02 13:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=10)),
                ('unit_price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='', max_length=30)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2024, 7, 2, 13, 17, 52, 214519))),
                ('dish', models.ManyToManyField(to='inventory.menuitem')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='menuitem',
            name='requirement',
            field=models.ManyToManyField(to='inventory.reciperequirement'),
        ),
    ]
