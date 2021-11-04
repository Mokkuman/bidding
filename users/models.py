from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_superuser(self, email, firstName, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        
        return self.create_user(email,firstName, password, **other_fields)
    
    
    def create_user(self, email, firstName, password, **other_fields):
        if not email:
            raise ValueError(_('Debes escribir un email'))
        
        email = self.normalize_email(email)
        user = self.model(email = email,  firstName = firstName, 
                          password = password, **other_fields)
        user.set_password(password)
        user.save()
        
        return user

        
class User(AbstractBaseUser, PermissionsMixin):
    #ID que es annadida por django por defecto
    firstName = models.CharField(max_length=100,blank=False)
    lastName = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, unique= True)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=64, blank = True)
    state = models.CharField(max_length=64,blank = True)
    money = models.PositiveIntegerField(blank=True,default=0)
    
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default=False) 
    #tal vez necesitemos enviar un correo de confirmacion idk xd
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName'] #email and password are required by default
    
    objects = UserManager()
    
    def __str__(self):
        return self.firstName + self.lastName

    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state

    def getMoney(self):
        return self.money