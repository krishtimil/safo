from django.shortcuts import render

# Create your views here.

def homepage(request, *args, **kwargs):
    return render(request, 'core/base.html')

def contactpage(request, *args, **kwargs):
    return render(request, 'core/base.html')
