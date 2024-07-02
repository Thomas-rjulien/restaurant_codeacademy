from django.db import models
import datetime

# Create your models here.

class Ingredient(models.Model):
	name = models.CharField(max_length=30)
	quantity = models.IntegerField(default=0)
	unit = models.CharField(max_length=10)
	unit_price = models.FloatField(default=0.0)

class RecipeRequirement(models.Model):
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)

class MenuItem(models.Model):
	price = models.FloatField(default=0.0)
	name = models.CharField(max_length=30)
	requirement = models.ManyToManyField(RecipeRequirement)

class Purchase(models.Model):
	customer_name = models.CharField(default="", max_length=30)
	dish = models.ManyToManyField(MenuItem)
	time_stamp = models.DateTimeField(default=datetime.datetime.now())


