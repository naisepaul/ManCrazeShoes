from django.contrib import admin
from .models import Product, ProductVariant, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('description',)
    list_display = ['name', 'category', 'price']
    list_filter = ['price', 'category']
    search_fields = ['name', 'price']

    ordering = ('-created_at',)


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'stock']
    list_filter = ['size', 'stock']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(Category)
