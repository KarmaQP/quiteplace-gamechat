from distutils.command.upload import upload
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account
from django import forms


class RegisterUserForm1(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'password1', 'password2',)


class RegisterUserForm(RegisterUserForm1):
  profile_image = forms.ImageField(label='Твоя аватарка', required=False)
