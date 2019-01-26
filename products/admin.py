from django.contrib import admin

# Register your models here.
from products.models import Product, Image, Category

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Category)
