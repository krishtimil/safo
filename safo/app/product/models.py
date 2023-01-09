from django.db import models
from django.contrib.auth.models import User
from app.vendor.models import Vendor
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    ordering = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['ordering']

    def __str__(self) -> str:
        return self.title
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='products/%Y/%m/%d/thumbnail/', blank=True, null=True)
    
    class Meta:
        ordering = ['added_date']
    
    def __str__(self) -> str:
        return self.title
    