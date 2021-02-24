from django.urls import path
from . import views

app_name = "origami"
urlpatterns = [
    path(route="", view=views.OrigamiHome, name="home"),
    path(route="list/", view=views.OrigamiListView.as_view(), name="list"),
]
