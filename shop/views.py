from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

"""The shop home page will display all products available for purchase"""
#Function to display the products on the front page for the shop
def home(request):
	#Context to display all of the products
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shop/home.html', context)



#Class to list the products
class ProductListView(ListView):
	model = Product
	template_name = 'shop/home.html'
	context_object_name = 'products'
	order = ['-date_posted']
	paginate_by = 9