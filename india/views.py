from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def kohli(request):
    return HttpResponse('<h1><marquee>kohli is the first cricketer to do 50 ODI centuries</marquee>')


def shami(request):
    return render(request,'shami.html')