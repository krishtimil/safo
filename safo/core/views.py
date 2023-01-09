from django.shortcuts import render

# Create your views here.

def homepage(request, *args, **kwargs):
    return render(request, 'core/test.html')

def contactpage(request, *args, **kwargs):
    return render(request, 'core/test.html')
