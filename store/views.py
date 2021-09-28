from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Hola pvtas")
    return render(request,"store/index.html")

def productListing(request):
    return HttpResponse("Products: ") #Solo es un ejemplo

def categories(request):
    return HttpResponse("Categories: ") #Solo es un ejemplo

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