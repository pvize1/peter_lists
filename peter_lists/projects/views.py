from django.views.generic import ListView
from django.db.models import Count
from django.shortcuts import render
from ..books.models import Book

# Create your views here.
def ProjHomeView(request):
    return render(request, "projects/home.html")


def ProjAdminView(request):
    return render(request, "projects/home.html")


class ProjTestView(ListView):
    model = Book
    data = Book.objects.all().order_by("-author")[:2]
    result = (
        Book.objects.values("author__name")
        .order_by("author__name")
        .annotate(count=Count("author__name"))
        .order_by("-count")[:10]
    )
    template_name = "projects/test.html"

    def get_queryset(self):
        # assert False
        return Book.objects.filter(type=3)
