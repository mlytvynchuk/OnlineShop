from django.shortcuts import render

# Create your views here.
from orders.models import Order
from products.models import Product


def product_list(request):
    viewtitle = "Shop"
    products = Product.objects.all()
    filtered_order = Order.objects.filter(owner=request.user.profile,is_ordered=False)
    current_order_products = []
    if filtered_order.exists():
        user_order = filtered_order[0]
        user_order_items = user_order.items.all()
        current_order_products = [item.product for item in user_order_items]
    context = {
        'products':products,
        'viewtitle':viewtitle,
        'current_order_products':current_order_products,
    }
    return render(request,'shop.html',context)