from django.urls.conf import path
from . import views

app_name = 'users'
urlpatterns = [
    path("login",views.loginV,name = "loginV"),
    path("signup", views.signup, name = "signup"),
    path("settings", views.goToSettings, name="settingsPage")
]
