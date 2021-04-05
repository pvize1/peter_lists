from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from peter_lists.books.models import Author, Book



class AuthorListView(ListView):
    model = Author
    paginate_by = 25
    template_name = "books/author_list.html"


class AuthorBookListView(ListView):
    model = Book
    paginate_by = 25
    template_name = "books/book_list.html"

    def get_queryset(self):
        self.author = get_object_or_404(Author, name=self.kwargs["author"])
        self.head = f"For Author = {self.author}"
        return Book.books.filter(author=self.author)
