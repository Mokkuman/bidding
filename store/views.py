from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BidProduct, Product,StockProduct
from store.forms import BidForm
from users.models import Bid

# Create your views here.

def cart(request):
    return render(request, "store/cart.html")

def goToBidProduct(request,id_product):
    product = BidProduct.objects.get(id=id_product)
    theForm = BidForm(instance=product)
    productCurrentBid = product.currentBid

    if request.method == "POST":
        theForm = BidForm(request.POST, instance=product)
        if not request.user.is_authenticated:
            return redirect('users:loginV')
        if theForm.is_valid():
            userMoney = request.user.money
            user_bid = theForm.cleaned_data['currentBid']
            print("userBid: "+str(user_bid))
            print("userMoney: "+str(userMoney))
            print("product current bid: "+str(productCurrentBid))
            if user_bid < userMoney and user_bid > productCurrentBid:
                theForm.save()
                newBid = Bid.objects.create(user = request.user, userBid = user_bid, product=product)
                print("BID SUCCESSFUL!") #use JavaScript alert() or some other UI notification
            else:
                print("YOU DONT HAVE ENOUGH MONEY OR YOUR BID IS TOO LOW")
    return render(request, "store/bidProductTemplate.html", {"product" : product, "form":theForm})

def goToStockProduct(request,id_product):
    product = StockProduct.objects.get(id=id_product)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('users:loginV')
        else:
            #Establecer relacion con el producto
            #Agregar al carrito
            #Bajar disponibilidad
            print("Compra exitosa!") #use JavaScript alert() or some other UI notification
    return render(request, "store/stockProductTemplate.html", {"product" : product})

def uploadProduct(request):
    return render(request,"store/uploadProduct.html")
