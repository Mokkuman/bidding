from django.http import response
from django.shortcuts import get_object_or_404, redirect, render
from .cart import Cart
from cart.models import Order,OrderItem
from store.models import BidProduct, StockProduct
from django.http import JsonResponse
from users.models import Bid, SystemNotification, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from cart.forms import OrderForm,OrderItemForm
import string
import random

# Create your views here.

#Vista del carrito
def cartSummary(request):
    cart = Cart(request)
    if not request.user.is_authenticated:
        return render(request,'store/cart.html',{'cart':cart})
    bids = Bid.objects.filter(user=request.user)
    bid=[]
    for b in bids:
        if not b.product.sold:
            bid.append(b)
    return render(request,'store/cart.html',{'cart':cart,
                                             'biddedProducts':bid})
    

#Agrega al carrito el producto de stock
def cartAdd(request):
    cart = Cart(request)
    print("Hola")
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(StockProduct,id=product_id)
        if product.inventory > 0:
            cart.add(product=product)
            #product.inventory-=1 Hacer esto en el checkout
            #product.save()
            response = JsonResponse({'test':'data'})
            #print("Compra exitosa!") use JavaScript alert() or some other UI notification
            messages.success(request,"No puedes ingresar valores negativos")
        else:
            #print("No hay stock!")
            messages.warning(request,"No hay stock!");
            return render(request, "store/stockProductTemplate.html", {'product' : product})
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

def checkout(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        if cart.__len__()==0:
            return redirect('cart:cartSummary')
        elif request.user.money>=cart.get_total_price():
            products_id=list(cart.cart.keys())
            for id in products_id:#Para comprobar si hay suficiente stock
                if cart.get_qty(str(id))>StockProduct.objects.get(id=id).inventory:
                    print("No hay suficiente stock")
                    return redirect("cart:cartSummary")
            if request.method == "POST":
                form = OrderForm(request.POST)
                if form.is_valid():#Verificar la longitud del número de teléfono ingresado ( 0< número/1,000,000,000 <10)
                    phone = float(form.cleaned_data['phone'])
                    if (phone/(1000000000)>=1) and (phone/(1000000000)<10):
                        order = form.save(commit=False)
                        order.orderKey = ''.join(random.choice(string.ascii_letters + string.digits )for i in range (15) )
                        order.totalPaid = cart.get_total_price()
                        order.user = request.user
                        order.save()
                        print(order)
                        request.method="GET"
                        return checkoutConfirmation(request)
                    else:
                        pass#Mandar alerta que el usuario ingresó un número incorrecto
            form = OrderForm()
            return render(request,"store/checkout.html",{'form':form})
        else:
            #print("Sin dinero suficiente!")
            messages.warning(request,"No hay dinero suficiente");
            return redirect('users:addMoney')
    #print("No permitido, debes iniciar sesión")
    messages.warning(request,"No permitido, debes iniciar sesión") #checar
    return HttpResponseNotAllowed("Not allowed")

def checkoutConfirmation(request):
    cart = Cart(request)
    if request.user.is_authenticated and cart.get_total_price()!=0:
        order = Order.objects.filter(user=request.user).last()#Puede generar errores
        if request.method == "POST":
            if "buy" in request.POST:
                products_id=list(cart.cart.keys())
                for id in products_id:
                    products = StockProduct.objects.get(id=id)
                    seller = products.seller
                    orderItem = OrderItem(order=order,product=products)
                    orderItem.price = cart.get_price(str(id))
                    orderItem.quiantity=cart.get_qty(str(id))
                    orderItem.save()
                    products.inventory -=cart.get_qty(str(id))  #Reduce el inventario
                    products.sold +=cart.get_qty(str(id))
                    products.save()
                    request.user.money -=cart.get_price(str(id))
                    request.user.save()
                    seller.money += cart.get_price(str(id))
                    newMessage = f'Has realizado una venta! Ve más detalles en el apartado de "Mis productos"'
                    SystemNotification.objects.create(toUser = seller, message = newMessage)
                    seller.save()
                newMessage = f'Su orden con clave: {order.orderKey} ha sido procesado! Puede checar en Mis Compras localizado en el header!'
                SystemNotification.objects.create(toUser = request.user, message = newMessage)
                cart.deleteAll()
                return redirect("users:myProducts")    
            else:
                cart.deleteAll()
                order.delete()
                return redirect('core:index')
        return render(request,"store/checkoutConfirmation.html",{"cart":cart,"order":order})
    return HttpResponseNotAllowed("Not allowed")