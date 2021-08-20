from django.db.models import fields
from rest_framework import serializers
from Coupon.models import Coupon

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'