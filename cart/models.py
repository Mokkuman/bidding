from django.db import models
from users.models import User
from store.models import Product,StockProduct,BidProduct

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order_user')
    fullName = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    totalPaid = models.FloatField(max_length=50)
    orderKey = models.CharField(max_length=200)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(StockProduct,related_name='order_items',on_delete=models.CASCADE)
    price = models.FloatField(max_length=50,default=1.0)
    quiantity = models.PositiveIntegerField(default=1)
    
class OrderBid(models.Model):
    order = models.ForeignKey(Order,related_name='bid',on_delete=models.CASCADE)
    product = models.ForeignKey(BidProduct,related_name='bidProduct',on_delete=models.CASCADE)
    price = models.FloatField(max_length=50,default=1.0)