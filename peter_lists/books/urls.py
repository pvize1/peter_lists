from django.urls import path
from .views import views_books, views_authors, views_publishers

app_name = "books"
urlpatterns = [
    path(route="", view=views_books.BookListView.as_view(), name="list"),
    path(route="add/", view=views_books.BookCreateView.as_view(), name="add"),
    path(route="update/<slug:slug>/", view=views_books.BookUpdateView.as_view(), name="update"),
    path(route="detail/<slug:slug>/", view=views_books.BookDetailView.as_view(), name="detail"),

    path(route="booktype/", view=views_books.BookTypeListView.as_view(), name="booktype_list"),
    path(route="booktype/books/<int:type_id>/", view=views_books.BookTypeBookListView.as_view(),
         name="booktype_book_list"),

    # Authors
    path(route="authors/", view=views_authors.AuthorListView.as_view(), name="author_list"),
    path(route="author/books/<author>/", view=views_authors.AuthorBookListView.as_view(), name="author_book_list"),

    # Publishers
    path(route="publishers/", view=views_publishers.PublisherListView.as_view(), name="publishers_list"),
    path(route="publisher/books/<publisher>/", view=views_publishers.PublisherBookListView.as_view(),
         name="publisher_book_list"),
]
