from django.urls import path
from . import views

urlpatterns = [
  path('login', views.LoginPageView.as_view(), name='login-page'),
  path('logout', views.logout_user, name='logout-page'),
  path('registration', views.register_user, name='registration-page')
]
