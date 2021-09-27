from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("productXXX", views.goToProduct, name="productPage")
]