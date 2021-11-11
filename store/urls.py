from django.urls import path
from . import views

app_name = 'store' #Para hacer las conexiones correspondientes entre templates de diferentes apps
# More info
# https://docs.djangoproject.com/en/3.0/intro/tutorial03/#namespacing-url-names

urlpatterns = [
    #path("cart",views.cart,name="cart"),
    path("bid/<int:id_product>/", views.goToBidProduct, name="bidProductPage"),
    path("stock/<int:id_product>/", views.goToStockProduct, name="stockProductPage"),
    path("uploadProduct",views.BidProductCreateView.as_view(),name="uploadProduct"),
]