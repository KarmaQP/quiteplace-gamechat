from email.policy import default
from django.db import models
from django.core.validators import MinLengthValidator as MinLen
from django.core.validators import MaxLengthValidator as MaxLen

# Create your models here.


class Role(models.Model):
  caption = models.CharField(max_length=100)

  def __str__(self):
    return self.caption


class User(models.Model):
  username = models.CharField(max_length=12)
  password = models.CharField(max_length=30)
  profile_image = models.ImageField(
    upload_to='images', default='images/avatar.jpg')
  date_of_reg = models.DateTimeField(auto_now_add=True)
  role = models.ForeignKey(
    Role, on_delete=models.SET_NULL, related_name='roles', default=2, null=True)

  def __str__(self):
    return self.username


class Message(models.Model):
  text = models.TextField(max_length=300)
  date = models.DateTimeField(auto_now=True)
  username = models.ForeignKey(
    User, on_delete=models.SET_NULL, related_name='messages', null=True)

  # def __str__(self):
  #   return self.username
