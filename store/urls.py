from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("products",views.productListing,name="productListing"),
    path("categories",views.categories,name="categories"),
    path("productXXX", views.goToProduct, name="productPage"),
]