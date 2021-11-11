from django.db import models
from users.models import Bid,User

# Create your models here.

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(isActive=True)

class Product(models.Model):
    productName = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    image = models.ImageField()
    objects = models.Manager()
    products = ProductManager()
    seller = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

    def __str__(self):
        return self.productName
    
    def getDescription(self):
        return self.description

    def getCategory(self):
        return self.category
    
    def getImage(self):
        return self.image


class BidProduct(Product):
    currentBid = models.PositiveIntegerField(blank=True,default=0)
    minBid = models.PositiveIntegerField(default=0)
    condition = models.CharField(max_length=50)
    bidWinner = models.OneToOneField(User, related_name="BidWinner", null=True, on_delete=models.SET_NULL, blank=True)

    #createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bidCreator",null=True)

    def save(self, *args, **kwargs):
        if not self.currentBid:
            self.currentBid = self.minBid
        super(BidProduct, self).save(*args, **kwargs)
    
    def getCurrentBid(self):
        return self.currentBid

    def getMinBid(self):
        return self.minBid

    def getCondition(self):
        return self.condition

    def getBidWinner(self):
        return self.bidWinner

class StockProduct(Product):
    price = models.FloatField(max_length=50)
    inventory = models.PositiveIntegerField(blank=True,default=1)
    #createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="productCreator",null=True)

    def getPrice(self):
        return self.price

    def getInventory(self):
        return self.inventory