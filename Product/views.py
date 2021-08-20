from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from Product.models import Category, ProductDetails, ProductVariation
from Product.serizlizers import ProductSerializer, CategorySerializer, ProductVariationSerializer
# Create your views here.

app_name = 'Product'

class CategoryList(APIView):

    def get(self, request):
        query = Category.objects.all()
        serializer = CategorySerializer(query, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CategorySerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowProduct(APIView):
    def get(self, request, id):
        query = ProductDetails.objects.filter(categoryKey=id)
        serializer = ProductSerializer(query, many=True)
        return Response(serializer.data)


class ShowProductDetails(APIView):
    
    def get(self, request, id):
        
        query_for_color = ProductVariation.objects.filter(productID=id,type='Color')
        colorData = ProductVariationSerializer(query_for_color, many=True)

        query_for_size = ProductVariation.objects.filter(productID=id,type='Size')
        sizeData = ProductVariationSerializer(query_for_size, many=True)

        query_for_product = ProductDetails.objects.get(id=id)
        productData = ProductSerializer(query_for_product)

        return Response({"Color" : colorData.data , "Size" : sizeData.data, "product" : productData.data})