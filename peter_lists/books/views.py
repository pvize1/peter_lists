from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "../templates/books/book_list.html"

class BookDetailView(DetailView):
    model = Book
    template_name = "../templates/books/book_detail.html"

