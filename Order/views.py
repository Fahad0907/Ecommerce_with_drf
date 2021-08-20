from Product.serizlizers import ProductSerializer
from django.shortcuts import render
from Order.models import Order, Cart
from Order.serializers import OrderSerializer, CartSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404 
from Product.models import ProductDetails
from Coupon.models import Coupon
from django.utils import timezone
# Create your views here.

app_name = 'Order'

class ShowCart(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        pid = data['item']
        quantity = int(data['quantity'])
        size = data['size']
        color = data['color']
        print(pid, quantity, size, color)
        item = ProductDetails.objects.get(id=pid)
        check_item_in_cart = Cart.objects.get_or_create(item=item, user=request.user, purchased=False
                                                        , size=size, color=color)
        check_order = Order.objects.filter(user=request.user, ordered=False)
        if check_order.exists():
            check_order = check_order[0]
            if check_order.orderItems.filter(item=item):
                check_item_in_cart[0].quantity += quantity
                check_item_in_cart[0].save()
                check_order.orderItems.add(check_item_in_cart[0])
            else:
                check_order.orderItems.add(check_item_in_cart[0])
                check_item_in_cart[0].quantity = quantity
                check_item_in_cart[0].save()
        else:
            check_item_in_cart[0].quantity = quantity
            check_item_in_cart[0].save()
            order = Order.objects.create(user=request.user)
            order.orderItems.add(check_item_in_cart[0])


        return Response({'message':'Data accepted'})
    

    def get(self, request):
        orderQuery = Order.objects.filter(user = request.user, ordered=False)
        if orderQuery.exists():
            orderQuery[0].amount = orderQuery[0].get_total_price()
            orderQuery[0].save() 
            
            serializer = OrderSerializer(orderQuery ,many=True)
            s = serializer.data[0]
            for i in s['orderItems']:
                #print(i['item'])
                product = ProductDetails.objects.get(id = i['item'])
                productSerializer = ProductSerializer(product)
                i['productInfo'] = productSerializer.data
             
           

            return Response(s)


class IncrementQuantity(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        order = Order.objects.filter(user=request.user, ordered=False)
        if order.exists():
            order = order[0]
            check_cart = Cart.objects.get(item=data['id'], purchased=False)
            check_cart.quantity += 1
            check_cart.save()
            order.orderItems.remove(check_cart)
            order.orderItems.add(check_cart)
            return Response({"message" : "Done"})

class DecrementQuantity(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order = Order.objects.filter(user=request.user, ordered=False)
        if order.exists():
            order = order[0]
            data = request.data
            check_cart = Cart.objects.get(item=data['id'], purchased=False)

            if check_cart.quantity <= 1:
                order.orderItems.remove(check_cart)
                check_cart.delete()
                return Response({"message" : "Done"})
            
            else:
                check_cart.quantity -= 1
                check_cart.save()
                order.orderItems.remove(check_cart)
                order.orderItems.add(check_cart)
                return Response({"message" : "Done"})

class ApplyCoupon(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        coupon_code = data['coupon']
        check_coupon = Coupon.objects.filter(code = coupon_code)
        order = Order.objects.filter(user=request.user, ordered=False)
    
        if check_coupon.exists() and order.exists() and order[0].couponCode is  None:
            
            current_time = timezone.now()
            if check_coupon[0].endTime >= current_time and check_coupon[0].active:
                discount = (float(check_coupon[0].discount) * order[0].get_total_price()) / 100
                order.update(amount = order[0].get_total_price() - discount, couponCode=coupon_code,discount=check_coupon[0].discount)
                
               
                return Response({"message":"Done"})
        else:
            return Response({"message":"Invalid Coupon"})


class CheckOut(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        print(data['payment'])
        cart = Cart.objects.filter(user=request.user, purchased=False)
        order = Order.objects.filter(user=request.user, ordered=False)
        if cart.exists() and order.exists():
            order.update(orderId ='zAq' + str(order[0].id) + 'tsw',paymentType=data['payment'],ordered=True)
            
            cart.update(purchased=True)
           
            return Response({"message":"Done"})
        else:
            return Response({"message":"Problem"})