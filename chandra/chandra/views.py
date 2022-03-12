from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello")


def education(request):
    return render(request, 'education.html')

def address(request):
    return render(request, 'address.html')

def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')



def capfirst(request):
    return HttpResponse("capital first <a href='/'>back</a>")
