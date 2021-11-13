from django.shortcuts import render
from users.models import User
from .forms import UpdateForm, UpdateMoneyForm, UserForm, LoginForm
from store.models import BidProduct,StockProduct
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
            newUser = theForm.save(commit=False)
            newUser.save()
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

def wishlist(request):
    return render(request,"users/wishlist.html")

@login_required
def myProducts(request):
    context={
        'bidProducts':BidProduct.objects.filter(seller=request.user),
        'stockProducts':StockProduct.objects.filter(seller=request.user)
    }
    return render(request,"users/myProducts.html",context)

def notifications(request):
    return render(request,"users/notifications.html")