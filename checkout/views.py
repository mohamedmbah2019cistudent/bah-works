from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, MakePaymentForm
from django.contrib import messages
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from shop.models import Product
import stripe
import logging

stripe.api_key = settings.STRIPE_SECRET

#Loggin used to find errors as I was 
logger = logging.getLogger(__name__)
"""Home view for the shop checkout"""

@login_required()
def checkout(request):
    logger.error('1. Entering Checkout')
    #Two different forms created for the user information and payment form
    if request.method == "POST":
        logger.error('2. Entering Post')
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        #Check that both forms are valid
        if payment_form.is_valid() and order_form.is_valid():
            logger.error('3. Entering Valid')
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.product_price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()

            try:
                logger.error('4. Entering Stripe')
                #logging.info(str(int(total * 100)))
                customer = stripe.Charge.create(
                    amount = int(total * 100), 
                    currency = "GBP", 
                    description = request.user.email, 
                    card = payment_form.cleaned_data['stripe_id']
                )
                
            except stripe.error.CardError:
                logger.error('4b. Stripe Failed')
                messages.error(request, 'Your card has been declined.')

            #If statement to determine which message to print
            if customer.paid:
                logger.error('5. Success (paid)')
                messages.error(request, 'Thanks for your payment, it has been successfully processed.')
                request.session['cart'] = {}
                return redirect(reverse('shop-home'))
            else:
                logger.error('5b. Failed')
                messages.error(request, 'We were unable to accept your payment.')

        #Message to print of forms are not valid
        else:
            print(payment_form.errors)
            messages.error(request, 'We were unable to accept a payment with the credit or debit card you provided.')
    
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, 'checkout/home.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})