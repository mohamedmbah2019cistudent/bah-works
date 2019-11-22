from django.shortcuts import get_object_or_404
from .models import JobFileUpload

"""Function to make sure that the products in the cart are maintained even when rendering other pages"""
def file_upload_contents(request):
    uploaded_file = request.session.get('cart', {})
    cart_items = []
    total = 0
    for id in uploaded_file.items():
        product = get_object_or_404(JobFileUpload, pk=id)
        total == product.file_price
        cart_items.append({'id': id, 'product': product})

    return {'file_name': file_name, 'file_price': file_price}