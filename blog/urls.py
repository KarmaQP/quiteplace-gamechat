from django.urls import path
from . import views

urlpatterns = [
  path('', views.AllBlogsPage.as_view(), name='blog-page'),
  path('<slug:slug>', views.DetailBlogPage.as_view(), name='detail-blog-page'),
]
