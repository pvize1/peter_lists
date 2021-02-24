from django.urls import path
from . import views

app_name = "passwd"
urlpatterns = [
    path("", views.PasswdHome, name="home"),
    path("display/", views.PasswdDisplay, name="display"),
]
