from django.core.paginator import Paginator
from django.views.generic import ListView
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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in extra data
        author = get_object_or_404(Author, name=self.kwargs["author"])
        p = Paginator(Book.books.filter(author=author), 25)
        context['page_obj'] = p.page(1)
        context['head'] = f"For Author = {author}"
        return context
