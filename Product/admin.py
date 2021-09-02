from django.contrib import admin
from Product.models import Category, ProductDetails , ProductVariation, Variation
# Register your models here.
admin.site.register(Category)
admin.site.register(ProductDetails)
admin.site.register(ProductVariation)
admin.site.register(Variation)