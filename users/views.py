from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.models import User
from .models import Account

# Create your views here.


class LoginPageView(View):
  def get(self, request):
    return render(request, 'users/login.html')

  def post(self, request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect('/')
    else:
      print('Error')
      return render(request, 'users/login.html')


def logout_user(request):
  logout(request)
  return HttpResponseRedirect('/')


def register_user(request):
  if request.method == 'POST':
    form = RegisterUserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      return HttpResponseRedirect('/')
    else:
      return render(request, 'users/register.html', {
        'form': form
      })
  else:
    form = RegisterUserForm()
    return render(request, 'users/register.html', {
      'form': form,
    })
