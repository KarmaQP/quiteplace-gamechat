from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
  user = models.OneToOneField(
    User, on_delete=models.CASCADE, related_name='users')
  profile_image = models.ImageField(upload_to='images')

  def __str__(self):
    return self.user.username
