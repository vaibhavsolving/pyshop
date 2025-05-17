from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)          #2083 is standard character of url don't use very large url


class Offer(models.Model):
    code = models.CharField(max_length=11)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
