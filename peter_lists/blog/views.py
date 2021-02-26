from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog


# Create your views here.
def BlogHome(request):
    return render(request, "blog/blog_home.html")


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
