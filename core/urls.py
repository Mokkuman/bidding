from django.urls.conf import path
from . import views

app_name = 'core'
urlpatterns = [
    path("",views.index,name="index"),
    path("FAQ",views.FAQ,name="FAQ"),
]
