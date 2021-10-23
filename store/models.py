from django.db import models

# Create your models here.

class Product(models.Model):
    #IDProduct = models.IntegerField()
    productName = models.CharField(max_length=50)
    price = models.FloatField(max_length=50)
    description = models.CharField(max_length=200)
    condition = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField()
    currentBid = models.CharField(max_length=50)

    def __str__(self):
        return self.productName
    
    # def getID(self):
    #     return self.IDProduct

    def getPrice(self):
        return self.price
    
    def getDescription(self):
        return self.description

    def getCategory(self):
        return self.category
    
    def getImage(self):
        return self.image

    def getCurrentBid(self):
        return self.currentBid
    
    def getCondition(self):
        return self.condition


