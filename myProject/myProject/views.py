from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('Hi, You are at Home Page.')
    return render(request, 'website/index.html')

def contact(request):
    #return HttpResponse('Hi, You are at Contact Us Page.')
    return render(request, 'website/contact.html')

def about(request):
    #return HttpResponse('Hi, You are at About Us Page.')
    return render(request, 'website/about.html')