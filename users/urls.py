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
    path("myProduts",views.myProducts,name="myProducts"),
    path("notifications",views.notifications,name="notifications"),
    path('deleteUserNotification/<notification_id>', views.deleteUserNotification, name="deleteUserNotification"),
    path('deleteBidNotification/<notification_id>', views.deleteBidNotification, name="deleteBidNotification"),
    path('deleteSystemNotification/<notification_id>', views.deleteSystemNotification, name="deleteSystemNotification"),
    path("deleteUser",views.deleteUser,name="deleteUser"),
    path("myProducts/<int:id_product>/updateStockProduct",views.UpdateStockGeneral.as_view(),name="updateStock"),
    path("myProducts/<int:id_product>/updateBidProduct",views.UpdateBidGeneral.as_view(),name="updateBid"),
    path("myShoppings",views.myShoppings,name="myShoppings"),
]
