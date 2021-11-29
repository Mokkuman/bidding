from django.shortcuts import render,redirect
#from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from .models import BidProduct, Product,StockProduct
from store.forms import BidForm, BidProductForm,StockProductForm
from users.models import Bid, User
from django.views.generic.edit import CreateView

from django.contrib import messages
# Create your views here.

def cart(request):
    return render(request, "store/cart.html")

def goToBidProduct(request,id_product):
    product = BidProduct.objects.get(id=id_product)
    theForm = BidForm(instance=product)
    productCurrentBid = product.currentBid
    if product.isActive and product.bidWinner==None:#Condición para saber si sigue activo (Cuando termine la puja o el usuario así lo decida)
        print(product.bidWinner)#Debe mostrar None en terminal
        if request.method == "POST":
            theForm = BidForm(request.POST, instance=product)
            if not request.user.is_authenticated:
                return redirect('users:loginV')
            if theForm.is_valid():
                userMoney = request.user.money
                if(theForm.cleaned_data['currentBid'] < 0):
                    messages.warning(request,"No puedes hacer una puja con dinero negativo")
                else:
                    user_bid = theForm.cleaned_data['currentBid']
                    print("userBid: "+str(user_bid))
                    print("userMoney: "+str(userMoney))
                    print("product current bid: "+str(productCurrentBid))
                    if user_bid < userMoney and user_bid > productCurrentBid:
                        try:
                            #Puede generarse un error donde no exista el Bid
                            bid = Bid.objects.get(user=request.user,product=product)
                            print("Sobreescribiendo puja")
                            bid.userBid = user_bid
                            bid.save()
                        except:
                            print("Creando puja")
                            newBid = Bid.objects.create(user = request.user, userBid = user_bid, product=product)
                        theForm.save()
                        #print("BID SUCCESSFUL!") #use JavaScript alert() or some other UI notification
                        messages.success(request,"Puja exitosa")
                
                    else:
                        #print("YOU DONT HAVE ENOUGH MONEY OR YOUR BID IS TOO LOW")
                        messages.warning(request,"No tienes suficientes fondos o tu puja es muy baja")
        product = BidProduct.objects.get(id=id_product)
        theForm = BidForm(instance=product)
        return render(request, "store/bidProductTemplate.html", {"product" : product, "form":theForm})
    return HttpResponseNotAllowed("Not allowed")

def goToStockProduct(request,id_product):
    product = StockProduct.objects.get(id=id_product)
    if product.isActive:
        return render(request, "store/stockProductTemplate.html", {"product" : product})
    else:
        print("No puedes entrar! El usuario decidió que ya no está activo el producto")
        return HttpResponseNotAllowed("Not allowed")

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
        if( form.cleaned_data['minBid'] < 0):
            #print("No puedes ingresar valores negativos")
            messages.warning(self.request,"No puedes ingresar valores negativos")
            return redirect("store:uploadBidProduct")
        else:
            bidProduct.save()
            return redirect("core:index")

class StockProductCreateView(CreateView):
    model = StockProduct
    form_class = StockProductForm
    template_name = 'store/uploadStockProduct.html'
    
    def form_valid(self,form):
        stockProduct = form.save(commit=False)
        stockProduct.seller = User.objects.get(id=self.request.user.id)
        if( form.cleaned_data['price'] < 0):
            #print("No puedes ingresar valores negativos")
            messages.warning(self.request,"No puedes ingresar valores negativos")
            return redirect('store:uploadStockProduct')
        else:
            stockProduct.save()
            return redirect('core:index')