from django.urls import path
from . import views

app_name = "projects"
urlpatterns = [
    path(route="", view=views.ProjHomeView.as_view(), name="home"),
]
