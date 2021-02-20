from django.views.generic import ListView, DetailView, CreateView
from .models import Book, Author, Publisher


class AuthorListView(ListView):
    model = Author
    template_name = "books/author_list.html"


class PublisherListView(ListView):
    model = Publisher
    template_name = "books/publisher_list.html"


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"


class BookCreateView(CreateView):
    model = Book
    template_name = "books/book_form.html"
    fields = [
        "title",
        "subtitle",
        "description",
        "author",
        "type",
        "form",
        "status",
    ]
