from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
app_name = "orders"
urlpatterns = [
    # path('cart/', cart,name = "cart"),
    path('add-to-cart/<item_id>/',add_to_cart,name="add_to_cart"),
    path('cart/', order_summary, name="order_summary"),
    path('delete-from-cart/<item_id>/',delete_from_cart,name="delete_from_cart"),
    path('checkout/',checkout,name="checkout"),

              ]\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_URL)