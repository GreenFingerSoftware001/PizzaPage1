from django.db import models

# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=90)
    lastname = models.CharField(max_length=90)
    email_field = models.CharField(max_length=120)
    addres = models.CharField(max_length=200)


class ProductDetail(models.Model):
    ProductName = models.CharField(max_length=90)
    product_price = models.IntegerField()
    product_image = models.ImageField()
    product_details = models.CharField(max_length=300)


class Products(models.Model):
    nameProduct = models/CharField(max_length=90)