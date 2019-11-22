from django.urls import path
from .views import ProductListView
from . import views

"""Urls for the shops app. These urls will be added to the '/shop' extension set up within the main site urls file in the 'cadwork' folder"""
urlpatterns = [
    path('', ProductListView.as_view(), name='shop-home'),
]