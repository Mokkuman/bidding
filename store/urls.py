from django.urls import path
from . import views

app_name = 'store' #Para hacer las conexiones correspondientes entre templates de diferentes apps
# More info
# https://docs.djangoproject.com/en/3.0/intro/tutorial03/#namespacing-url-names

urlpatterns = [
    path("cart",views.cart,name="cart"),
    path("productXXX", views.goToProduct, name="productPage"),
    path("uploadProduct",views.uploadProduct,name="uploadProduct"),
]