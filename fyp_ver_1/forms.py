from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Contact


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {'message': forms.Textarea(attrs={'rows': 4, 'cols': 20}),}
        fields = ['name', 'email', 'subject', 'message']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_buyer = forms.BooleanField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'is_buyer']


