from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """

    recent_items = Product.objects.order_by('-created_at')[:6]

    context = {
        'recent_items': recent_items,
    }
    return render(request, 'home/index.html', context)


def about_us(request):
    """ A view to return the about us page """

    return render(request, 'home/aboutus.html')


def faq(request):
    """ A view to return the about us page """

    return render(request, 'home/faq.html')


def privacy_policy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy_policy.html')
