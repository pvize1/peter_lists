from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path(route="", view=views.BookListView.as_view(), name="list"),
    path(route="add/", view=views.BookCreateView.as_view(), name="add"),
    path(route="update/<slug:slug>/", view=views.BookUpdateView.as_view(), name="update"),
    path(route="<slug:slug>/", view=views.BookDetailView.as_view(), name="detail"),
    path(route="booktype/", view=views.BookTypeListView.as_view(), name="booktype_list"),
    path(route="booktype/books/<int:type_id>/", view=views.BookTypeBookListView.as_view(), name="booktype_book_list"),
    path(route="authors/", view=views.AuthorListView.as_view(), name="author_list"),
    path(route="author/books/<author>/", view=views.AuthorBookListView.as_view(), name="author_book_list"),
    path(route="publishers/", view=views.PublisherListView.as_view(), name="publishers_list"),
    path(route="publisher/books/<publisher>/", view=views.PublisherBookListView.as_view(), name="publisher_book_list"),
]
