from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField
from profiles.models import UserProfile
# Create your models here.


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('formal', 'Formal Shoes'),
        ('casual', 'Casual Shoes'),
        ('sandals', 'Sandals'),
    ]
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return dict(self.CATEGORY_CHOICES)[self.name]

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    SIZE_CHOICES = [
        ('40/6', 'Size 40/6'),
        ('41/7', 'Size 41/7'),
        ('42/8', 'Size 42/8'),
        ('43/9', 'Size 43/9'),
        ('44/10', 'Size 44/10'),
        ('45/11', 'Size 45/11'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    # Example range of 0 to 20
    stock = models.IntegerField(validators=[MinValueValidator(0),
                                MaxValueValidator(20)])

    def __str__(self):
        return f"{self.product.name} - {self.size}"


class Wishlist(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"