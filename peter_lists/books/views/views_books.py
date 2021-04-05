from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Count
from django.shortcuts import get_object_or_404
from peter_lists.books.models import Book, BookType
from peter_lists.books.forms import EditBookForm


class BookListView(ListView):
    model = Book
    paginate_by = 25
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"


class BookCreateView(LoginRequiredMixin, CreateView):
    form_class = EditBookForm
    model = Book
    action = "Add"
    template_name = "books/book_form.html"


class BookUpdateView(LoginRequiredMixin, UpdateView):
    form_class = EditBookForm
    model = Book
    action = "Edit"
    template_name = "books/book_form.html"


class BookTypeListView(ListView):
    model = BookType
    result = (
        Book.books.values("type", "type__type")
        .order_by("type__type")
        .annotate(count=Count("type__type"))
        .order_by("-count")[:10]
    )
    template_name = "books/booktype_list.html"


class BookTypeBookListView(ListView):
    model = BookType
    paginate_by = 25
    template_name = "books/book_list.html"

    def get_queryset(self):
        self.booktype = get_object_or_404(BookType, id=self.kwargs["type_id"])
        self.head = f"For Type = {self.booktype.type}"
        return Book.books.filter(type=self.booktype.id)
