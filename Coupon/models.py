from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=15, unique=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code