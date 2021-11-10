from django.shortcuts import render
from store.models import StockProduct,BidProduct

# Create your views here.
def index(request):
    return render(request,"core/index.html")

def FAQ(request):
    return render(request,"core/FAQ.html")

def index(request):
	context = {
        'stockProducts':StockProduct.objects.all(),
        'bidProducts':BidProduct.objects.all()
    }
	return render(request,'core/index.html',context)