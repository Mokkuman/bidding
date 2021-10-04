from django.shortcuts import render

# Create your views here.
def loginV(request):
    return render(request,"users/login.html")
        
def signup(request):
    pass