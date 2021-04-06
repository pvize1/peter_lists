from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from peter_lists.books.models import Publisher, Book


class PublisherListView(ListView):
    model = Publisher
    paginate_by = 25
    template_name = "books/publisher_list.html"


class PublisherBookListView(ListView):
    model = Book
    #lookup_url_kwarg = "publisher"
    #lookup_field = "publisher"
    paginate_by = 25
    template_name = "books/book_list.html"

    @property
    def publisher(self):
        return get_object_or_404(Publisher, name=self.kwargs["publisher"])

    def get_queryset(self):
        return Book.books.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in extra data
        context['head'] = f"For Publisher = {self.publisher}"
        return context
