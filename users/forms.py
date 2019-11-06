from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

class UserForm(UserCreationForm):
    helper = FormHelper()
    title = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ['username', 'title', 'password1', 'password2']