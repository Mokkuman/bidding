from django.http import response
from django.shortcuts import get_object_or_404, redirect, render
from .cart import Cart
from store.models import BidProduct, StockProduct
from django.http import JsonResponse
from users.models import Bid, User
# Create your views here.

#Vista del carrito
def cartSummary(request):
    cart = Cart(request)
    if not request.user.is_authenticated:
        return render(request,'store/cart.html',{'cart':cart})
    bids = Bid.objects.filter(user=request.user)
    return render(request,'store/cart.html',{'cart':cart,
                                             'biddedProducts':bids})
    

#Agrega al carrito el producto de stock
def cartAdd(request):
    cart = Cart(request)
    print("Hola")
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(StockProduct,id=product_id)
        if product.inventory > 0:
            cart.add(product=product)
            product.inventory-=1
            product.save()
            response = JsonResponse({'test':'data'})
            #print("Compra exitosa!") use JavaScript alert() or some other UI notification
        else:
            print("No hay stock!")
            return render(request, "store/stockProductTemplate.html", {"product" : product})
        return response
    
def cartDelete(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)
        cartTotal = cart.get_total_price()
        response = JsonResponse({'subtotal':cartTotal})
        return response
    
def deleteBid(request, bid_id):
    bid = Bid.objects.get(pk = bid_id)
    bidProduct = bid.product
       
    bid.delete()
    if not Bid.objects.filter(product = bidProduct):
        print("No hay bidders. CurBid = minBid")
        bidProduct.currentBid = bidProduct.minBid
    else:
        prevBid = Bid.objects.all().last()
        bidProduct.currentBid = prevBid.userBid
        print("CurBid actualizada a la última puja")
    bidProduct.save()
    return redirect('cart:cartSummary')