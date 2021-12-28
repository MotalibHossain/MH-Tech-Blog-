from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'Login_User/login.html')


def registrations(request):
    return render(request, 'Login_user/registrations.html')


def Profile(request):
    return render(request, 'Login_user/profile.html')