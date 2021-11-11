from django.urls import path

from . import views
app_name='cart'

urlpatterns=[
    path('',views.cartSummary,name='cartSummary'),
    path('add/',views.cartAdd,name='cartAdd'),
    path('delete/',views.cartDelete,name='cartDelete'),
]