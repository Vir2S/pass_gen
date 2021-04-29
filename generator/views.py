from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    pwd_len = int(request.GET.get('length', 10))
    pwd = ''

    for char in range(pwd_len):
        pwd += random.choice(characters)

    return render(request, 'generator/password.html', {'password': pwd})
