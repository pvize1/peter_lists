from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path(route="", view=views.BlogHome, name="home"),
    path(route="list", view=views.BlogListView.as_view(), name="list"),
    path(route="add/", view=views.BlogCreateView.as_view(), name="add"),
    path(route="<int:pk>/update/", view=views.BlogUpdateView.as_view(), name="update"),
]
