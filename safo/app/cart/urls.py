from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('success/', views.success, name="success"),
]
