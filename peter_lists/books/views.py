from django.views.generic import ListView, DetailView, CreateView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "../templates/books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "../templates/books/book_detail.html"


class BookCreateView(CreateView):
    model = Book
    template_name = "../templates/books/book_form.html"
    fields = [
        "title",
        "subtitle",
        "description",
        "author",
        "type",
        "form",
        "status",
    ]
