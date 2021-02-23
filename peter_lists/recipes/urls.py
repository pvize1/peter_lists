from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path(route="", view=views.RecipeListView.as_view(), name="list"),
]
