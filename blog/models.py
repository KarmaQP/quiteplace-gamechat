from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
  caption = models.CharField(max_length=20)

  def __str__(self):
    return self.caption


class Author(models.Model):
  username = models.CharField(max_length=100)

  def __str__(self):
    return self.username


class Post(models.Model):
  title = models.CharField(max_length=100)
  excerpt = models.CharField(max_length=150)
  image = models.ImageField(upload_to='posts', null=True)
  date = models.DateTimeField(auto_now_add=True)
  slug = models.SlugField(unique=True, db_index=True)
  content = models.TextField()
  author = models.ForeignKey(
    Author, on_delete=models.SET_NULL, null=True, related_name='posts')
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.title


class Comment(models.Model):
  user = models.ForeignKey(
    User, on_delete=models.CASCADE, null=True, related_name="comments")
  text = models.TextField(max_length=400)
  post = models.ForeignKey(
    Post, on_delete=models.CASCADE, related_name='comments')
