from django.urls import path
from . import views

app_name = "lego"
urlpatterns = [
    path(route="", view=views.LegoHome, name="home"),
    path(route="list/", view=views.LegoListView.as_view(), name="list"),
]
