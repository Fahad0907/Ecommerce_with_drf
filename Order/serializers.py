from django.db import models
from django.db.models import fields
from Order.models import Cart, Order
from rest_framework import serializers
from Product.serizlizers import ProductSerializer

app_name = 'Order'

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1
    


class OrderSerializer(serializers.ModelSerializer):
   
    class Meta :
        model = Order
        fields ='__all__'
        depth = 1
    
    
    
    