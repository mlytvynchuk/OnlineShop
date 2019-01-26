from django.db import models

class Image(models.Model):
    image = models.ImageField(default="default.png",upload_to="products_pics")
    alt = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    images = models.ManyToManyField(Image, related_name="images")
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name="category")
    def __str__(self):
        return self.name


