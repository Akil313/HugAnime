from django.forms import ModelForm
from .models import AnimeCatalog
from django.contrib.auth.models import User
from django import forms

class AnimeCatalogForm(ModelForm):
    class Meta:
        model = AnimeCatalog
        exclude = ()


#login form
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']