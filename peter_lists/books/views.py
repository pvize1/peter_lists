from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Book, Author, Publisher


class AuthorListView(ListView):
    model = Author
    template_name = "books/author_list.html"


class PublisherListView(ListView):
    model = Publisher
    template_name = "books/publisher_list.html"


class BookListView(ListView):
    paginate_by = 25
    model = Book
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
    action = "Update"
