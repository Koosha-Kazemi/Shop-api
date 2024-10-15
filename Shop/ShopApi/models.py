from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    stock = models.BooleanField()
