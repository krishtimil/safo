from django.shortcuts import render

# Create your views here.
def vendors(request, *args, **kwargs):
    return render(request, 'core/test.html')

def become_vendor(request, *args, **kwargs):
    return render(request, 'core/test.html')

def edit_vendor(request, *args, **kwargs):
    return render(request, 'core/test.html')

def add_product(request, *args, **kwargs):
    return render(request, 'core/test.html')

def vendor(request, *args, **kwargs):
    return render(request, 'core/test.html')

def vendor_admin(request, *args, **kwargs):
    return render(request, 'core/test.html')



