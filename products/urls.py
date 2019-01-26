
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
app_name = "products"
urlpatterns = [
    path('',home,name="home"),
    path('products/',product_list,name="product_list"),
]\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

