from django.test import TestCase
from django.apps import apps

# Imports for app tests
from .apps import ShopConfig

#Imports for views testing
from .models import Product

# Create your tests here.
# Testing the app for the blog section
class TestShopConfig(TestCase):

    def test_shop_app(self):
        self.assertEqual("shop", ShopConfig.name)
        self.assertEqual("shop", apps.get_app_config("shop").name)

#Testing a model for the products in the shop
class TestShopModels(TestCase):

    def test_product(self):
        product = Product(product_name='Product', product_description='Product description test', product_price=2.00)
        product.save()
        self.assertEqual(product.product_name, 'Product')
        self.assertEqual(product.product_description, 'Product description test')
        self.assertEqual(product.product_price, 2.00)

#Testing the shop views
class TestShopViews(TestCase):

    def get_shop_home_view(self):
        shop_home = self.client.get("/shop/")
        self.assertEqual(shop_home.status_code, 200)
        self.assertTemplateUsed(shop_home, "shop/home.html")