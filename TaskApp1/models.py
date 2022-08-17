from itertools import product
from operator import mod
from xml.dom.minidom import Document
from django.db import models

# Create your models here.

class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=500)
    ProductDescription = models.CharField(max_length=500)
    ProductRemark = models.CharField(max_length=500)
    ProductDocument = models.FileField(upload_to='pdf/')  
    ProductVideo = models.URLField(max_length = 500)
    ProductSource = models.URLField(max_length = 500)   
    productDate = models.DateField(auto_now_add=True)
    
    
class HScode(models.Model):
    HsId = models.AutoField(primary_key=True)
    HsCode = models.IntegerField()
    HsDescription = models.CharField(max_length=500)
    HsRemark = models.CharField(max_length=500)
    HsDocument = models.FileField(upload_to='pdf/')
    HsVideo = models.URLField(max_length = 500)
    HsSource = models.URLField(max_length = 500)   
    HsDate = models.DateField(auto_now_add=True)
    product = models.ManyToManyField(Product)
    