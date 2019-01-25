from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from accounts.models import Profile
from orders.extras import generate_order_id
from orders.models import Order, OrderItem
from products.models import Product
from django.contrib import messages


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


def add_to_cart(request,**kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()

    order_item, status = OrderItem.objects.get_or_create(
        product=product
    )
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()
    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('products:product_list'))

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('orders:order_summary'))

@login_required()
def order_summary(request, **kwargs):
    existing_order = get_user_pending_order(request)
    if request.POST:
        for item in existing_order.items.all():
            item_quantity = request.POST.get('quantity'+str(item.id), '')
            item.quantity = item_quantity
            item.save()
        return redirect(reverse('orders:checkout'))
    context = {
        'order': existing_order
    }


    return render(request, 'cart.html', context)

def checkout(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'checkout.html', context)