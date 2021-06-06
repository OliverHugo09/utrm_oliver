from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hola mundo')

def first_app(request):
    return HttpResponse('<h1>My FirstApp</h1>')