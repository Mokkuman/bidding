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

class Person(models.Manager):
    IDPerson = models.IntegerField(max_length=50)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    def __str__(self):
        return self.firstName + self.lastName
    
    def getID(self):
        return self.IDPerson

