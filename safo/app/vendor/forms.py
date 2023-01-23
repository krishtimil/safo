from django.forms import ModelForm, models

from app.product.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']