from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from .models import Book, Author, Publisher


class AuthorListView(ListView):
    model = Author
    paginate_by = 25
    template_name = "books/author_list.html"


class AuthorBookListView(ListView):
    model = Book
    paginate_by = 25
    template_name = "books/book_list.html"
    head = "For Author ="

    def get_queryset(self):
        self.author = get_object_or_404(Author, name=self.kwargs['author'])
        return Book.objects.filter(author=self.author)


class PublisherListView(ListView):
    model = Publisher
    paginate_by = 25
    template_name = "books/publisher_list.html"


class PublisherBookListView(ListView):
    model = Book
    paginate_by = 25
    template_name = "books/book_list.html"
    head = "For Publisher ="

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

class BookListView(ListView):
    model = Book
    paginate_by = 25
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "books/book_form.html"
    fields = [
        "title",
        "subtitle",
        "description",
        "author",
        "publisher",
        "type",
        "form",
        "status",
    ]
    action = "Add"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "books/book_form.html"
    fields = [
        "title",
        "subtitle",
        "description",
        "author",
        "publisher",
        "type",
        "form",
        "status",
    ]
    action = "Edit"
