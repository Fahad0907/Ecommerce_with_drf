"""Ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Order.models import Order
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Product.views import CategoryList, ShowProduct,  ShowProductDetails
from Order.views import  ShowCart,IncrementQuantity, DecrementQuantity, ApplyCoupon, CheckOut
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',CategoryList.as_view()),
    path('showproduct/<int:id>/', ShowProduct.as_view()),
    path('productDetails/<int:id>/', ShowProductDetails.as_view()),
    path('login/', obtain_auth_token),
    path('cart/', ShowCart.as_view()),
    path('plus/', IncrementQuantity.as_view()),
    path('minus/',DecrementQuantity.as_view()),
    path('coupon/',ApplyCoupon.as_view()),
    path('checkout/',CheckOut.as_view())
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)