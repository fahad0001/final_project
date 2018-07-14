from django import forms
from .models import Product


class NewPro(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description','price', 'image','category', 'store',)
