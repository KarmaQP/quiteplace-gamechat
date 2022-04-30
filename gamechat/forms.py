from email.policy import default
from django import forms
from .models import User


class RegisterForm(forms.Form):
  username = forms.CharField(label="Имя пользователя", max_length=12, error_messages={
    'required': 'Имя пользователя не должно быть пустым',
    'max_length': 'Please enter a shorter name'
  })
  password = forms.CharField(label='Пароль', max_length=50, widget=forms.PasswordInput(), error_messages={
    'required': 'Пароль введи плз',
    'max_length': 'Норм у тебя пароль, покороче выбери'
  })
  # profile_image = forms.ImageField(label='Ава профиля', required=False, error_messages={
  #   'required': 'Нужна картинка???'
  # })

# class RegisterForm(forms.ModelForm):
#   class Meta:
#     model = User
#     exclude = ['role']
