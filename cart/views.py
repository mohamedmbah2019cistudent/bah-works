from django.shortcuts import render, redirect, reverse

"""Create your views here."""
#Render the products within the cart page in the same way as the shop home page
def home(request):
    return render(request, 'cart/home.html')
    


#Function to add the quantities of products
def add_to_cart(request, pk):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if pk in cart:
        cart[pk] = int(cart[pk]) + quantity
    else:
        cart[pk] = cart.get(pk, quantity)
    request.session['cart'] = cart
    return redirect(reverse('cart-home'))



#Function in the cart to allow the user to be able to change the quantity in the cart.
def adjust_cart(request, pk):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    #If statement to check the quantity of products. If they are 0 product to be removed from the cart page.
    if quantity > 0:
        cart[pk] = quantity
    else:
        #cart.pop(pk)
        cart[pk] = 0

    request.session['cart'] = cart
    return redirect(reverse('cart-home'))