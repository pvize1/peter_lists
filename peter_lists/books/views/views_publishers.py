from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from peter_lists.books.models import Publisher, Book


class PublisherListView(ListView):
    model = Publisher
    paginate_by = 25
    template_name = "books/publisher_list.html"


class PublisherBookListView(ListView):
    model = Book
    paginate_by = 25
    template_name = "books/book_list.html"

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs["publisher"])
        self.head = f"For Publisher = {self.publisher}"
        return Book.books.filter(publisher=self.publisher)
