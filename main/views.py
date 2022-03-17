from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


def layout(request):
    return render(request, 'main/layout.html')


def dashboard(request):
    return render(request, 'main/dashboard.html')


def home(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('dashboard')  # Redirect to a success page.

    return render(request, 'main/home.html', {'login_form': form})


def about(request):
    return render(request, 'main/about.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'main/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    redirect('layout')
