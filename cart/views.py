from django.http import response
from django.shortcuts import get_object_or_404, render
from .cart import Cart
from store.models import StockProduct
from django.http import JsonResponse
# Create your views here.

def cartSummary(request):
    cart = Cart(request)
    return render(request,'store/cart.html',{'cart':cart})

def cartAdd(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(StockProduct,id=product_id)
        cart.add(product=product)
        response = JsonResponse({'test':'data'})
        #Bajar disponibilidad
        #print("Compra exitosa!") use JavaScript alert() or some other UI notification
        return response
    
def cartDelete(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)
        cartTotal = cart.get_total_price()
        response = JsonResponse({'subtotal':cartTotal})
        return response