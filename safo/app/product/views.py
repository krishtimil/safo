from django.shortcuts import render

# Create your views here.
def search(request, *args, **kwargs):
    return render(request, 'core/test.html')

def product(request, *args, **kwargs):
    return render(request, 'core/test.html')

def category(request, *args, **kwargs):
    return render(request, 'core/test.html')


