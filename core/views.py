from django.shortcuts import render
from store.models import StockProduct,BidProduct

# Create your views here.
def index(request):
    return render(request,"core/index.html")

def FAQ(request):
    return render(request,"core/FAQ.html")

def index(request):
	context = {
        'stockProducts':StockProduct.objects.filter(isActive = True),
        'bidProducts':BidProduct.objects.filter(isActive=True)
    }
	return render(request,'core/index.html',context)