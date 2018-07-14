from django import forms
from .models import Store


class NewStore(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name','description', 'lat', 'long', 'type', )
