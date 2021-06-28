from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'ejercicio/home.html',{'nombre':'oliver lucero'})

def create_password(request):
    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        caracteres.extend(list('0123456789'))
    if request.GET.get('special'):
        caracteres.extend(list('@#$%&*()'))
    length = int(request.GET.get('length',8))
    pswd = ''
    for x in range(length):
        pswd += random.choice(caracteres)
    return render(request,'ejercicio/password.html',{'password':pswd})