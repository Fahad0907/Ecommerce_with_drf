from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    productName = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    discountVal = models.IntegerField()
    available = models.BooleanField(default=True)
    categoryKey = models.ForeignKey(Category, on_delete=models.CASCADE)

   

    def __str__(self):
        return self.productName
    
class ProductVariation(models.Model):
    productID = models.ForeignKey(ProductDetails, on_delete=models.CASCADE) 
    type = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.type