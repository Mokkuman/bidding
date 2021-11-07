from django.db import models
from users.models import Bid

# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    image = models.ImageField()

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
    bidWinner = models.OneToOneField(Bid, null=True, on_delete=models.SET_NULL, blank=True)

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

    def getPrice(self):
        return self.price

    def getInventory(self):
        return self.inventory