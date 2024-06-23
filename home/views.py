from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """

    recent_items = Product.objects.order_by('-created_at')[:6]
    return render(request, 'home/index.html', {'recent_items': recent_items})


def about_us(request):
    """ A view to return the about us page """

    return render(request, 'home/aboutus.html')
