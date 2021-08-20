from django.shortcuts import render
from Order.models import Cart, Order
from Order.serializers import CartSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from Product.models import ProductDetails
from Product.serizlizers import ProductSerializer
from Account.serializers import UserSerializer
# Create your views here.

app_name = "Account"



class OrderList(APIView):
    def get(request, self):
        order_query = Order.objects.filter(user=request.user).order_by('delivered')
        if order_query.exists():
            pass

class Registration(APIView):
    def post(self, request):
        serializers = UserSerializer(data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'error': False, 'message' : 'usersuccess full', 'data' : serializers.data})
        return Response({'error': True, 'message' : 'A user with that username already exist'})