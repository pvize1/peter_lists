from django.urls import path
from . import views

app_name = "passwd"
urlpatterns = [
    path("", views.home, name="home"),
    path("display/", views.display, name="display"),
]
