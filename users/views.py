from django.shortcuts import render
from users.models import BidNotification, User,Bid, UserNotification, SystemNotification
from .forms import UpdateForm, UpdateMoneyForm, UserForm, LoginForm,UpdateBid,UpdateStock
from store.models import BidProduct,StockProduct
from cart.models import Order, OrderItem,OrderBid
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.http import HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def loginV(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, email=email,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('core:index')
        else: #User doesn't exist
            return render(request,"users/login.html",{"form":form,"msg":'No existe el usuario'})
            
    return render(request,"users/login.html",{"form":form})
        
def signup(request):
    if request.method == "POST":
        theForm = UserForm(request.POST) #get the form filled out 
        if theForm.is_valid():
            adminEmail = "droseher@gmail.com"
            newUser = theForm.save(commit=False)
            newUser.save()
            newMessage = f"Bienvenido {newUser.firstName}! Gracias por crear una cuenta PulgApp!"
            from_user = User.objects.get(email=adminEmail)
            UserNotification.objects.create(toUser = newUser, message = newMessage, fromUser = from_user)
            login(request,newUser)
            return redirect('core:index')
    else:
        theForm = UserForm()
    return render(request, "users/signup.html", {"form":theForm})
    
def logoutUser(request):
    logout(request)
    return redirect("users:loginV")

@login_required
def goToProfile(request):
    # if request.method == "POST":
    #     return redirect('users:updateProfile')
    curret_user = request.user
    #userName = curret_user.lastName
    return render(request, "users/myProfile.html",{'user':curret_user})

@login_required
def updateProfile(request):
    if request.method == "POST":
        if 'UpdateProfile' in request.POST:
            theForm = UpdateForm(request.POST,request.FILES,instance=request.user)
            theForm.actual_user=request.user 
            if theForm.is_valid():
                theForm.save()
                return redirect('users:myProfile')
        else:
            return redirect('users:myProfile')
    else:
        data={'firstName':request.user.firstName,'lastName':request.user.lastName,
            'city':request.user.city,'state':request.user.state}
        theForm = UpdateForm(None,initial=data)
        return render(request,"users/updateProfile.html",{"form":theForm})
    
@login_required
def deleteUser(request):
    if request.method=="POST":
        if "delete" in request.POST:
            user = User.objects.get(email=request.user.email)
            user.is_active = False
            user.save()
            logout(request)
            return redirect('core:index')
        else:
            return redirect('users:myProfile')        
    return render(request,"users/deleteUser.html")

@login_required
def updateMoney(request):
    if request.method=="POST":
        if "UpdateMoney" in request.POST:
            theForm = UpdateMoneyForm(request.POST,instance=request.user)
            mon1 = request.user.money
            if theForm.is_valid():
                mon = theForm.cleaned_data['money']
                theForm.actual_user = request.user
                theForm.actual_user.money = mon1 + mon
                theForm.save()
                return redirect('users:myProfile')
        else:
            return redirect('users:myProfile')
    theForm = UpdateMoneyForm()
    return render(request,"users/addMoney.html",{"form":theForm})

@login_required
def myProducts(request):
    context={
        'bidProducts':reversed(BidProduct.objects.filter(seller=request.user)),
        'stockProducts':reversed(StockProduct.objects.filter(seller=request.user))
    }
    return render(request,"users/myProducts.html",context)

class UpdateStockGeneral(DetailView):
    form_class = UpdateStock
    template_name = "users/updateMyStockProduct.html"
    
    def get(self,request, *args, **kwargs):
        try:
            product = StockProduct.objects.get(id=kwargs['id_product'],seller=request.user)
            data={'productName':product.productName,'description':product.description,
                'category':product.category,'price':product.price,'inventory':product.inventory
                ,'isActive':product.isActive}
            self.form_class.initial = data
            form = self.form_class(initial=data)
            return render(request,"users/updateMyStockProduct.html",{"form":form})
        except:
            return HttpResponseNotAllowed("Not allowed")
    
    def post(self,request,*args, **kwargs):
        if "UpdateProduct" in request.POST and (not "Delete" in request.POST):
            print("Dentro de UpdateProduct")
            form = UpdateStock(request.POST,request.FILES,instance=StockProduct.objects.get(id=kwargs['id_product']))
            if form.is_valid():
                if(form.cleaned_data['price']<0):
                    messages.warning(self.request,"No puedes ingresar valores negativos")
                else:                
                    form.save()
                    return redirect('users:myProducts')
            return render(request,self.template_name,{'form':form})
        elif "Delete" in request.POST:
            #Parte para eliminar el producto
            print("Dentro de Eliminar")
            product = StockProduct.objects.get(id=kwargs['id_product'])
            product.delete()
            return redirect('users:myProducts')
        elif "Orders" in request.POST:
            return orders(request,kwargs['id_product'])
        else:
            print("Dentro de cancelar")
            return redirect('users:myProducts')
        
def orders(request,id_product):
    orderItem = reversed(OrderItem.objects.filter(product = id_product))
    return render(request,"users/orders.html",{"orderItem":orderItem})

def order(request,id_order):
    orderItem = OrderItem.objects.get(id = id_order)
    if request.user.id != orderItem.product.seller.id:
        return HttpResponseNotAllowed("Not allowed")
    else:
        if request.method=="POST":
            orderItem.shipped = True
            orderItem.save()
            print(orderItem.shipped)
            return redirect('users:myProducts')
        return render(request,"users/order.html",{"orderItem":orderItem})
        
class UpdateBidGeneral(DetailView):
    form_class = UpdateBid
    template_name = "users/updateMyStockProduct.html"
    
    def get(self,request, *args, **kwargs):
        try:
            product = BidProduct.objects.get(id=kwargs['id_product'],seller=request.user)
            data={'productName':product.productName,'description':product.description,
                'category':product.category,'isActive':product.isActive}
            self.form_class.initial = data
            form = self.form_class(initial=data)
            return render(request,"users/updateMyBidProduct.html",{"form":form,"bid":product})
        except:
            print("No puedes acceder a esta página porque no eres el propietario del producto")
            return HttpResponseNotAllowed("Not allowed")
    
    def post(self,request,*args, **kwargs):
        if "UpdateProduct" in request.POST:
            print("Dentro de UpdateProduct")
            form = UpdateBid(request.POST,request.FILES,instance=BidProduct.objects.get(id=kwargs['id_product']))
            if form.is_valid():
                form.save()
                return redirect('users:myProducts')
            return render(request,self.template_name,{'form':form})
        elif "End" in request.POST:
            #Parte para escoger ganador de bid
            product = BidProduct.objects.get(id = kwargs['id_product'])
            bid = Bid.objects.filter(product = product.id)
            
            for b in bid:
                bidder = b.user
                if b.userBid == product.currentBid:
                    product.bidWinner = b.user
                    product.isActive = False
                    product.sold = True
                    product.save()
                    print("Producto actualizado, ganador seleccionado")
                    print("Ahora el producto no es visible")
                    #Enviar notificacion al ganador
                    newMessage = f'¡Felicidades {b.user.firstName}! ¡Has ganado el bid para el producto: {product.productName}! ¡Vendido a ${product.currentBid}! Comuníquese con {product.seller.email}, por favor.'
                    #BidNotification.objects.create(toUser = bidder, message = newMessage, fromBidProduct = product)    
                else:
                    #Enviar notificaciones a los perdedores
                    newMessage = f'Lo sentimos, {b.user.firstName}. El bid del producto:  {product.productName} ha concluido y NO ganaste.'
                    b.delete()
                BidNotification.objects.create(toUser = bidder, message = newMessage,fromBidProduct = product)
            return redirect('users:myProducts')
        elif "Delete" in request.POST:
            #Parte para eliminar producto
            print("Dentro de eliminar")
            product = BidProduct.objects.get(id = kwargs['id_product'])
            bid = Bid.objects.filter(product = product.id)
            bid.delete()
            product.delete()
            return redirect('users:myProducts')
        else:
            print("Dentro de cancelar")
            return redirect('users:myProducts')
        
@login_required
def notifications(request):
    userNotifications = reversed(UserNotification.objects.filter(toUser = request.user))
    bidNotifications = reversed(BidNotification.objects.filter(toUser = request.user))
    systemNotifications = reversed(SystemNotification.objects.filter(toUser = request.user))
      
    return render(request,"users/notifications.html",{
        "notifications":userNotifications,
        "bidNotifications":bidNotifications,
        "systemNotifications":systemNotifications})
    
def deleteUserNotification(request, notification_id):
    notification = UserNotification.objects.get(id = notification_id)
    notification.delete()
    return redirect('users:notifications')
    
def deleteBidNotification(request, notification_id):
    notification = BidNotification.objects.get(id = notification_id)
    notification.delete()
    return redirect('users:notifications')
    
def deleteSystemNotification(request, notification_id):
    notification = SystemNotification.objects.get(id = notification_id)
    notification.delete()
    return redirect('users:notifications')

@login_required
def myShoppings(request):
    order = Order.objects.filter(user=request.user)
    aux=[]
    for o in order:
        orderItem = OrderItem.objects.filter(order=o)
        for i in orderItem:    
            aux.append(i)
    aux.reverse()
    bid=[]
    bids = Bid.objects.filter(user=request.user)
    for b in bids:
        product = b.product
        if product.bidWinner == request.user:
            bid.append(product)
    bid.reverse()
    return render(request,"users/myShoppings.html",{'order':aux,'bidProducts':bid})

def status(request,id_order):
    orderItem = OrderItem.objects.get(id = id_order)
    if request.user.id == orderItem.order.user.id:
        if request.method == "POST":
            return redirect('users:myShoppings')
        else:
            return render(request,"users/status.html",{"orderItem":orderItem})
    else:
        return HttpResponseNotAllowed("Not allowed")