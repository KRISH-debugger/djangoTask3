from dataclasses import fields
import imp
from rest_framework import serializers
from TaskApp1.models import Product,HScode

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('ProductId','ProductName','ProductDescription','ProductRemark','ProductDocument','ProductVideo','ProductSource','productDate')
        
class HScodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=HScode
        fields=('HsId','HsCode','HsDescription','HsRemark','HsDocument','HsVideo','HsSource','HsDate','product')