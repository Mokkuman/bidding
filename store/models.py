from django.db import models

# Create your models here.

class Product(models.Model):
    IDProduct = models.IntegerField()
    productName = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.productName
    
    def getID(self):
        return self.IDProduct


class Product(models.Model):
    IDProduct = models.IntegerField(max_length=50)
    productName = models.CharField(max_length=50)
    price = models.FloatField(max_length=50)
    description = models.CharField(max_length=200)
    condition = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField()
    currentBid = models.CharField(max_length=50)

    def __str__(self):
        return self.productName
    
    def getID(self):
        return self.IDProduct

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

class User(models.Model):
    IDUser = models.IntegerField(max_length=50)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName + self.lastName
    
    def getID(self):
        return self.IDUser

    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password

    def getAdress(self):
        return self.adress

class Admin(models.Manager):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def getPassword(self):
        return self.password

