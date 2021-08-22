from django.shortcuts import render
from rest_framework.serializers import Serializer
from Order.models import Cart, Order
from Order.serializers import CartSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from Product.models import ProductDetails
from Product.serizlizers import ProductSerializer
from Account.serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.

app_name = "Account"



class OrderList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        
        if data['ordered'] == 'True':
            order_query = Order.objects.filter(user=request.user)
        else:
            order_query = Order.objects.filter(user=request.user, delivered=False)
        
     
        if order_query.exists():
            order_query.order_by('delivered')
            serializer = OrderSerializer(order_query,many=True)
            
            return  Response( serializer.data)
        return  Response({"Message" : "Wrong"})
        
    def get(self,request):
        order_query = Order.objects.filter(user=request.user)
        if order_query.exists():
            countPendingOrder = Order.objects.filter(user=request.user, ordered=True, delivered=False)
            countTotal = Order.objects.filter(user=request.user, ordered=True)
            serizlizertPendingOrder = OrderSerializer(countPendingOrder,many=True)
            serizlizerTotal = OrderSerializer(countTotal,many=True)
            return Response({"Total":serizlizerTotal.data , "pending":serizlizertPendingOrder.data})
        return Response({"Message":"wrong"})

class Registration(APIView):
    def post(self, request):
        serializers = UserSerializer(data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'error': False, 'message' : 'usersuccess full', 'data' : serializers.data})
        return Response({'error': True, 'message' : 'A user with that username already exist'})

class UserInformation(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            query = User.objects.get(id= request.user.id)
            serializer = UserSerializer(query)
            return Response({"Data":serializer.data})
        except:
            return Response({"message":"Error"})


