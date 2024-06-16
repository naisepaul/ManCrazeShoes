from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductVariant


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['image']
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)
