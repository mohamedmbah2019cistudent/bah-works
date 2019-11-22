from django.test import TestCase
from django.apps import apps

# Imports for app tests
from .apps import CheckoutConfig

# Imports to test the models and views
from .models import Order, OrderLineItem

# Testing the app
class TestCheckoutConfig(TestCase):

    def test_checkouts_app(self):
        self.assertEqual("checkout", CheckoutConfig.name)
        self.assertEqual("checkout", apps.get_app_config("checkout").name)

#Testing a model for the checkout
class TestCheckout(TestCase):

    def test_checkout_order(self):
        order = Order(customer_name='Test Name', customer_address_line_one='1 Test Road', customer_address_town='Town', customer_address_county='County', customer_address_post_code='TE57 1ZE')
        order.save()
        self.assertEqual(order.customer_name, 'Test Name')
        self.assertEqual(order.customer_address_line_one, '1 Test Road')
        self.assertEqual(order.customer_address_town, 'Town')
        self.assertEqual(order.customer_address_county, 'County')
        self.assertEqual(order.customer_address_post_code, 'TE57 1ZE')

    def test_order_line_item(self):
        order_line_item = OrderLineItem(quantity=3)
        self.assertEqual(order_line_item.quantity, 3)

#Testing a model for the checkout
class TestCheckout(TestCase):

    def test_checkout_order(self):
        order = Order(customer_name='Test Name', customer_address_line_one='1 Test Road', customer_address_town='Town', customer_address_county='County', customer_address_post_code='TE57 1ZE')
        order.save()
        self.assertEqual(order.customer_name, 'Test Name')
        self.assertEqual(order.customer_address_line_one, '1 Test Road')
        self.assertEqual(order.customer_address_town, 'Town')
        self.assertEqual(order.customer_address_county, 'County')
        self.assertEqual(order.customer_address_post_code, 'TE57 1ZE')

    def test_order_line_item(self):
        order_line_item = OrderLineItem(quantity=3)
        self.assertEqual(order_line_item.quantity, 3)