from django.db import models
from shop.models import Product

"""Creating the models for the forms to be used in the checkout"""
#Order form to take the address of the user
class Order(models.Model):
    customer_name = models.CharField(max_length=25, blank=False)
    customer_address_line_one = models.CharField(max_length=40, blank=False)
    customer_address_town = models.CharField(max_length=40, blank=False)
    customer_address_county = models.CharField(max_length=40, blank=True)
    customer_address_post_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return 'Customer: {0}, name {1}, on {2}'.format(self.id, self.customer_name, self.date)



#Order to use foreign keys for the product and order
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return 'Order {0} {1} for £{2}'.format(self.quantity, self.product.product_name, self.product.product_price)
    