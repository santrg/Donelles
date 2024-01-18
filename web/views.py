from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def fotos(request):
    return render(request,'fotos.html')

def videos(request):
    return render(request,'videos.html')

def shows(request):
    return render(request,'shows.html')

def contacto(request):
    return render(request,'contacto.html')
