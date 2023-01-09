from django.shortcuts import render

# Create your views here.
def search(request, *args, **kwargs):
    return render(request, 'core/base.html')

def product(request, *args, **kwargs):
    return render(request, 'core/base.html')

def category(request, *args, **kwargs):
    return render(request, 'core/base.html')


