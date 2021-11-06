from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def cart(request):
    return HttpResponse("Carrito ") #Solo es un ejemplo

def goToProduct(request):
    try:
        dummyData = {
            'name':'Product 1XX',
            'currentBid':100,
            'description':'Very cool treasure box',
            'category':'TOYS',
            'condition':'LIKE NEW'
        }
        return render(request, 'store/productTemplate.html',{
            'product':dummyData,
            'productFound':True
        })
    except Exception as exception:
        return render(request, "store/productTemplate.html",{
            'productFound':False
        })