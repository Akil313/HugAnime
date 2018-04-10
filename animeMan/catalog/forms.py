from django.forms import ModelForm
from .models import AnimeCatalog
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login, get_user_model, logout

class AnimeCatalogForm(ModelForm):
    class Meta:
        model = AnimeCatalog
        exclude = ()


#Login form class
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password']

    #
    def clean(self, *args, **kwargs):
        #ensures data is changed to universal format
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        #ensure user exists
        user = authenticate(username = username, password = password)
        
        if username and password:
            #if user does not exist, give an error 
            if not user:
                raise forms.ValidationError("This user does not exist")
            #if password is not correct, give an error
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            #if user no longer exists, or is banned, give an error
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        

        return super(LoginForm, self).clean(*args, **kwargs)
