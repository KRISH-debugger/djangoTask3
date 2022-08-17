from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from TaskApp1.models import Product,HScode
from TaskApp1.Serializers import ProductSerializer,HScodeSerializer


# Create your views here.

@csrf_exempt
def productApi(request,id=0):
    if request.method=='GET':
        product = Product.objects.all()
        return render(request,"TaskApp1/product.html", {"product":product})
    
def hscodeapi(request):
    if request.method=='GET':
        hscode = HScode.objects.all()
        return render(request,"TaskApp1/hscode.html", {"hscode":hscode}) 

def home(request):
    return render(request,'TaskApp1/index.html')