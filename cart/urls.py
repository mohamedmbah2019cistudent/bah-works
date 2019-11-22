from django.urls import path
from .views import home, add_to_cart, adjust_cart

"""Urls for the cart section of the site. These urls will be added to the '/cart' extension set up within the main site urls file in the 'cadwork' folder"""
urlpatterns = [
    path('', home, name='cart-home'),
    #path('add/^(?P<id>\d+)/', add_to_cart, name='add_to_cart'),
    path('add/<int:pk>/', add_to_cart, name='add_to_cart'),
    #path('adjust/^(?P<id>\d+)/', adjust_cart, name='adjust_cart'),
    path('adjust/<int:pk>/', adjust_cart, name='adjust_cart')
]