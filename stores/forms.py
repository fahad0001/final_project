from django import forms
from .models import Store


class NewStore(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'lat', 'long', 'type')
        exclude = ('user', )
