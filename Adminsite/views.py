from django.db.models.query_utils import Q
from Product.serizlizers import CategorySerializer, ProductSerializer
from django.shortcuts import render
from Order.models import Order, Cart
from Order.serializers import OrderSerializer, CartSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404 
from Product.models import Category, ProductDetails, ProductVariation
from Coupon.models import Coupon
from django.utils import timezone
from rest_framework import status

# Create your views here.
app_name ="Adminsite"

class Addproduct(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        get_category_id = Category.objects.get(name=request.data['categoryKey'])
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(categoryKey_id=get_category_id.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        query = ProductDetails.objects.get(id=id)
        print(id)
        serializer = ProductSerializer( query, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    
    def get(self, request):
        query = Category.objects.all()
        serializer = CategorySerializer(query, many = True)
        return Response(serializer.data)

class UpdateProduct(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request, id):
        query_for_product = ProductDetails.objects.get(id=id)
        productData = ProductSerializer(query_for_product)
        return Response({ "product" : productData.data})
    def post(self, request):
        get_category_id = Category.objects.get(name=request.data['category'])
        query = ProductDetails.objects.filter(categoryKey=get_category_id )
        serializer = ProductSerializer(query, many=True)
        return Response(serializer.data)
    def put(self, request, id):
        query = ProductDetails.objects.get(id=id)
        print(request.data)
        serializer = ProductSerializer( query, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request):
       
        try :
            holdProduct = ProductDetails.objects.get(id=request.data['id'])
            holdProduct.delete()
            return Response({"message" : "ok"})
        except:
            return Response({"message" : "Error"})
    


