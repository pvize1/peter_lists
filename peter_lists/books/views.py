from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

