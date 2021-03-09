from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog


# Create your views here.
def BlogHome(request):
    blogs = Blog.objects.order_by("-date")[:3]
    return render(request, "blog/blog_home.html", {'blogs': blogs})


class BlogListView(ListView):
    model = Blog
    paginate_by = 3
    template_name = "blog/blog_list.html"
