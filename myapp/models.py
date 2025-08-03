from django.db import models

# Create your models here.
class Orderpy(models.Model):
    per_name= models.CharField(max_length=200)
    orderfood= models.CharField(max_length=200)
    orderdrink= models.CharField(max_length=200)
    food_price=models.IntegerField(default=0)
    drink_price=models.IntegerField(default=0)
    total_price=models.IntegerField(default=0)
