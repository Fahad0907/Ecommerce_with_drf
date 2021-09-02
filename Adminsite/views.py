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
         
        try:
            hold_request = request.data
            get_category_id = Category.objects.get(name=hold_request['categoryKey'])
            
            
            product = ProductDetails.objects.create(productName=hold_request['productName'],description=hold_request['description'],
            price=hold_request['price'], discountVal=hold_request['discountVal'], categoryKey=get_category_id, image=hold_request['image'])
            get_id = ProductDetails.objects.get(productName=hold_request['productName'])
          
            size = hold_request['size']
            size = size.split(",")

            for sizes in size:
                if sizes:
                    ProductVariation.objects.create(productID_id=get_id.id, type = 'Size',  value= sizes)
                

            colors = hold_request['color'].split(' ')
            for color in colors:
                ProductVariation.objects.create(productID_id=get_id.id, type = 'Color', value= color)
        
            return Response({"error":False, "message" : "done"})
        except:
            return Response({"error":True, "message" : "problem"})
    
    def get(self, request):
        query = Category.objects.all()
        serializer = CategorySerializer(query, many = True)
        return Response(serializer.data)

class UpdateProduct(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        get_category_id = Category.objects.get(name=request.data['category'])
        query = ProductDetails.objects.filter(categoryKey=get_category_id )
        serializer = ProductSerializer(query, many=True)
        return Response(serializer.data)
    def put(self, request):
        print(request.data['image'])
        
        return Response({"message" : "done"})

    def delete(self, request):
       
        try :
            holdProduct = ProductDetails.objects.get(id=request.data['id'])
            holdProduct.delete()
            return Response({"message" : "ok"})
        except:
            return Response({"message" : "Error"})
    



