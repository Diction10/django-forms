from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first = forms.CharField()
    last = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first', 'last', 'email', 'password1', 'password2']