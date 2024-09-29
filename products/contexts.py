from .models import Wishlist


def wishlist_count(request):
    """ Context processor to add wishlist count to all templates """
    if request.user.is_authenticated:
        profile = request.user.userprofile
        wishlist = Wishlist.objects.filter(user=profile).first()
        if wishlist:
            return {'wishlist_count': wishlist.products.count()}
    return {'wishlist_count': 0}
