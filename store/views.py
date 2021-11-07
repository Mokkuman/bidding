from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BidProduct, Product
from users.forms import BidForm
from users.models import Bid

# Create your views here.

def cart(request):
    return render(request, "store/cart.html")

def goToProduct(request):
    firstProduct = BidProduct.objects.first()
    theForm = BidForm(instance=firstProduct)
    productCurrentBid = firstProduct.currentBid

    if request.method == "POST":
        theForm = BidForm(request.POST, instance=firstProduct)
        if not request.user.is_authenticated:
            return redirect('users:loginV')
        if theForm.is_valid():
            userMoney = request.user.money
            user_bid = theForm.cleaned_data['currentBid']
            print("userBid: "+str(user_bid))
            print("userMoney: "+str(userMoney))
            print("product current bid: "+str(productCurrentBid))
            if user_bid <= userMoney and user_bid > productCurrentBid:
                theForm.save()
                newBid = Bid.objects.create(user = request.user, userBid = user_bid, product=firstProduct)
                print("BID SUCCESSFUL!") #use JavaScript alert() or some other UI notification
            else:
                print("YOU DONT HAVE ENOUGH MONEY OR YOUR BID IS TOO LOW")
    return render(request, "store/productTemplate.html", {"product" : firstProduct, "form":theForm})

def uploadProduct(request):
    return render(request,"store/uploadProduct.html")

