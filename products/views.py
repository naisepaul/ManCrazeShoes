from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, ProductVariant, Wishlist
from .forms import ProductForm, ProductVariantFormSet
# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all().order_by('-created_at')
    query = None
    categories = None
    sort = None
    direction = None
    new_arrivals = None    

    wishlist_products = []  # List of products in the user's wishlist
    wishlist_count = 0
    # If the user is authenticated, get their wishlist products
    if request.user.is_authenticated:
        profile = request.user.userprofile
        wishlist = Wishlist.objects.filter(user=profile).prefetch_related('products').first()
        if wishlist:
            wishlist_products = wishlist.products.all()  # Get the products in the user's wishlist
            wishlist_count = wishlist.products.count()
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'new_arrivals' in request.GET:
            products = products[:8]
            new_arrivals = True

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               f"You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # | Q(price__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    # Check if each product is in the user's wishlist
    products_with_wishlist_status = []
    for product in products:
        is_in_wishlist = product in wishlist_products if request.user.is_authenticated else False
        products_with_wishlist_status.append({
            'product': product,
            'is_in_wishlist': is_in_wishlist,
        })
        
    context = {
        'products': products,
        'products_with_wishlist_status': products_with_wishlist_status,
        'wishlist_count': wishlist_count,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'new_arrivals': new_arrivals,                
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    
    product = get_object_or_404(Product, pk=product_id)
    productvariant = ProductVariant.objects.filter(product=product)
    wishlist = False
    if request.user.is_authenticated:
        profile = request.user.userprofile    
        if Wishlist.objects.filter(user=profile, products=product).exists():
            wishlist = True   
                   
    context = {
        'product': product,
        'productvariant': productvariant,   
        'wishlist': wishlist,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        variant_formset = ProductVariantFormSet(request.POST)

        if product_form.is_valid() and variant_formset.is_valid():
            product = product_form.save()  # Save the Product
            
            # Iterate through each variant form
            for variant in variant_formset:
                if variant.cleaned_data and variant.cleaned_data['size']:  
                    variant_instance = variant.save(commit=False) 
                    variant_instance.product = product  
                    variant_instance.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))

    else:
        product_form = ProductForm()
        variant_formset = ProductVariantFormSet(queryset=ProductVariant.objects.none())

    return render(request, 'products/add_product.html', {
        'product_form': product_form,
        'variant_formset': variant_formset,
    })


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           f'Failed to update product. '
                           f'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def my_wishlist(request, pk):
    ''' Renders wishlist page '''
    profile = request.user.userprofile
    # wishlist = Wishlist.objects.filter(user=profile).order_by('created_at')
    wishlist = Wishlist.objects.filter(user=profile).first()    
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'products/wishlist.html', context)


@login_required
def wishlist_add(request, pk):
    ''' Adds products to favourites '''
    profile = request.user.userprofile
    product = get_object_or_404(Product, id=pk)
    redirect_url = request.POST.get('redirect_url','products')

    wishlist, created = Wishlist.objects.get_or_create(
        user=profile)    
    if product in wishlist.products.all():
        wishlist.products.remove(product)  # Remove the product if already in the wishlist
        messages.success(request, f'{product.name} removed from your wishlist')
    else:
        wishlist.products.add(product)  # Add the product to the wishlist
        messages.success(request, f'{product.name} added to your wishlist')  
    return redirect(redirect_url)


def place_order(request):
    if request.method == 'POST':
        size = request.POST.get('size')
        variant = get_object_or_404(ProductVariant, size=size)
        
        # Reduce stock only if it's available
        if variant.stock > 0:
            variant.stock -= 1  # Decrease stock by 1 (or the ordered quantity)
            variant.save()
            return redirect('products/product_detail', product_id=variant.product.id)  # Redirect to the product page
        else:
            return render(request, 'products/product_detail.html', {
                'error': 'Selected size is out of stock!',
                'product': variant.product,
                'productvariant': variant.product.productvariant_set.all()
            })