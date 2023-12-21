from django import forms
from django.core import validators
# signup form


class SignUp(forms.Form):
    username = forms.CharField(initial='Enter username',required=True )
    email = forms.CharField(initial='Enter your email',required=True, validators=[validators.EmailValidator(message="Invalid Email")] )
    password = forms.CharField(initial='Enter password',required=True)