from django.urls.conf import path
from . import views

app_name = 'users'
urlpatterns = [
    path("login",views.loginV,name = "loginV"),
    path("signup", views.signup, name = "signup"),
    path("profile", views.goToProfile, name="myProfile"),
    path("logoutUser", views.logoutUser, name = "logout"),
    path("updateProfile",views.updateProfile,name="updateProfile"),
    path("addMoney",views.updateMoney,name="addMoney"),
    path("wishlist",views.wishlist,name="wishlist"),
    path("myProduts",views.myProducts,name="myProducts"),
    path("notifications",views.notifications,name="notifications"),
]
