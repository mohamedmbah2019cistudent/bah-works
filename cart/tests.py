from django.test import TestCase
from django.apps import apps

#Imports for app testing
from .apps import CartConfig

# Testing the app
class TestCartConfig(TestCase):

    def test_cart_app(self):
        self.assertEqual("cart", CartConfig.name)
        self.assertEqual("cart", apps.get_app_config("cart").name)

# Testing the views for the cart home page
class TestCartViews(TestCase):

    def test_cart_page(self):
        cart_home = self.client.get("/cart/")
        self.assertEqual(cart_home.status_code, 200)
        self.assertTemplateUsed(cart_home, "cart/home.html")