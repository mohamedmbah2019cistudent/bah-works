from django.shortcuts import get_object_or_404
from shop.models import Product

"""Function to make sure that the products in the cart are maintained even when rendering other pages"""
def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.product_price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
