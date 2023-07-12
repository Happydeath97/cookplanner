from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms.widgets import DateInput

class UserRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'date_of_birth', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
