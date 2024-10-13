from django import forms

from shoppapp.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all())
    class Meta:
        model = Order
        fields = ['products']