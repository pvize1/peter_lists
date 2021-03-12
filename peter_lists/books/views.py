from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from .models import Book, Author, Publisher, BookType
from .forms import EditBookForm


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
        return Book.objects.filter(author=self.author)


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
        return Book.objects.filter(publisher=self.publisher)


class BookListView(ListView):
    model = Book
    book_types = BookType.objects.all().order_by('type')
    paginate_by = 25
    template_name = "books/book_list.html"

    def get_queryset(self):
        if self.kwargs.get("type_id"):
            qry = Book.objects.filter(type=self.kwargs["type_id"])
        else:
            qry = Book.objects.all()
        return qry


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"


class BookCreateForm(LoginRequiredMixin, CreateView):
    form_class = EditBookForm
    model = Book
    action = "Add"
    template_name = "books/book_form.html"


class BookUpdateForm(LoginRequiredMixin, UpdateView):
    form_class = EditBookForm
    model = Book
    action = "Edit"
    template_name = "books/book_form.html"
