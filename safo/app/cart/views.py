from django.shortcuts import render

# Create your views here.
def cart(request, *args, **kwargs):
    return render(request, 'core/base.html')

def success(request, *args, **kwargs):
    return render(request, 'core/base.html')

