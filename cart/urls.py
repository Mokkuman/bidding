from django.urls import path

from . import views
app_name='cart'

urlpatterns=[
    path('',views.cartSummary,name='cartSummary'),
    path('add/',views.cartAdd,name='cartAdd'),
    path('delete/',views.cartDelete,name='cartDelete'),
    path('deleteBid/<bid_id>', views.deleteBid, name="deleteBid"),
    path('cart/checkout',views.checkout, name="checkout"),
    path('cart/checkoutConfirmation',views.checkoutConfirmation, name="checkoutConfirmation"),
]