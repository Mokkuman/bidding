from django.shortcuts import render,redirect
from django.http import HttpResponse


from .models import BidProduct, Product,StockProduct
from store.forms import BidForm, BidProductForm,StockProductForm
from users.models import Bid, User
from django.views.generic.edit import CreateView

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
    return render(request, "store/stockProductTemplate.html", {"product" : product})

def selectProduct(request):
    return render(request,"store/uploadProduct.html")

class BidProductCreateView(CreateView):
    model = BidProduct
    form_class = BidProductForm
    template_name = 'store/uploadBidProduct.html'
    #success_url = 'uploadProduct'
    
    #def get_success_url(self):
     #   return reverse_lazy('product_list')
    
    def form_valid(self, form):
        bidProduct = form.save(commit=False)
        bidProduct.seller = User.objects.get(id=self.request.user.id) 
        bidProduct.save()
        return redirect("core:index")

class StockProductCreateView(CreateView):
    model = StockProduct
    form_class = StockProductForm
    template_name = 'store/uploadStockProduct.html'
    
    def form_valid(self,form):
        stockProduct = form.save(commit=False)
        stockProduct.seller = User.objects.get(id=self.request.user.id)
        stockProduct.save()
        return redirect('core:index')