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

    def __str__(self):
        return f'name : {self.name} price : {self.price}  discount : {self.discount} stock : {self.stock}'


class OptionProduct(models.Model):
    title = models.CharField(max_length=30)
    value = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} -> {self.title} : {self.value}'

