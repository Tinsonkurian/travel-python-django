from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def news(request):
    return render(request,'news.html')

def contact(request):
    return render(request, 'contact.html')
 
def elements(request):
    return render(request, 'elements.html')

def destinations(request):
    return render(request, 'destinations.html')