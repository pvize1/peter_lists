from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path(route="", view=views.BookListView.as_view(), name="list"),
    path(route="add/", view=views.BookCreateView.as_view(), name="add"),
    path(route="<slug:slug>/", view=views.BookDetailView.as_view(), name="detail"),
]
