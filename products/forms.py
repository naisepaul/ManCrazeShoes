from django import forms
from django.forms import modelformset_factory
from .models import Product, ProductVariant


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['size', 'stock']

        widgets = {
            'size': forms.Select(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }


ProductVariantFormSetAdd = modelformset_factory(
    ProductVariant,
    form=ProductVariantForm,
    extra=6,
)
ProductVariantFormSetEdit = modelformset_factory(
    ProductVariant,
    form=ProductVariantForm,
    extra=0,  # Show only existing variants
)
