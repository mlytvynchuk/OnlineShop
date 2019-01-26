from django.shortcuts import render

# Create your views here.
from orders.models import Order
from products.models import Product, Category


# def get_images(product):
#     images = ProductImages.objects.filter(product=product)
#     return images

def home(request):
    featured_category = Category.objects.filter(name="featured")[0]
    featured_products = featured_category.products.all()
    order_id = request.session.get("order_id", None)
    if order_id is None:  # and isinstance(order_id,int):
        print("create new order")
        existing_order = Order.objects.create(owner=None)
        request.session['order_id'] = existing_order.id

    else:
        print("It exists")
    viewtitle = "Home"
    products = Product.objects.all()
    filtered_order = Order.objects.filter(id=order_id, is_ordered=False)
    current_order_products = []
    if filtered_order.exists():
        user_order = filtered_order[0]
        user_order_items = user_order.items.all()
        current_order_products = [item.product for item in user_order_items]
    context = {
        'featured_products':featured_products,
        'current_order_products': current_order_products,

    }
    return render(request,'index.html',context)
def product_list(request):
    print(request.session)
    order_id = request.session.get("order_id", None)
    if order_id is None:  # and isinstance(order_id,int):
        print("create new order")
        existing_order = Order.objects.create(owner=None)
        request.session['order_id'] = existing_order.id

    else:
        print("It exists")
    viewtitle = "Shop"
    products = Product.objects.all()
    filtered_order = Order.objects.filter(id=order_id,is_ordered=False)
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