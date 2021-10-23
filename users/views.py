from django.shortcuts import render
#from store.models import User
from .models import User
from .forms import UserForm
from django.shortcuts import render, redirect

# Create your views here.
def loginV(request):
    return render(request,"users/login.html")
        
def signup(response):
    if response.method == "POST":
        theForm = UserForm(response.POST) #get the form filled out 
        if theForm.is_valid():
            newUser = theForm.save()
            print(newUser)
            return redirect('/')
    else:
        theForm = UserForm()
    return render(response, "users/signup.html", {"form":theForm})
    

def goToSettings(request):
    return render(request, "users/settingsTemplate.html")