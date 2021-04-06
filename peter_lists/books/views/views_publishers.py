from django.core.paginator import Paginator
from django.views.generic import ListView
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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in extra data
        publisher = get_object_or_404(Publisher, name=self.kwargs["publisher"])
        p = Paginator(Book.books.filter(publisher=publisher), 25)
        context['page_obj'] = p.page(1)
        context['head'] = f"For Publisher = {publisher}"
        return context
