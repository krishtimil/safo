from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.frontpage, name="home"),

    path('contact-us/', views.contactpage, name="contact"),
]
urlpatterns += staticfiles_urlpatterns()


