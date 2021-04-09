from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.db.models import Count
from django.urls import reverse_lazy
from .models import Blog
from .forms import EditBlogForm


# Create your views here.
def BlogHome(request):
    raw_tags = dict()
    blogs = Blog.blog.order_by("-modified")[:3]
    for record in Blog.blog.all():
        for t in record.tag.split(","):
            raw_tags[t.strip()] = raw_tags.get(t.strip(), 0) + 1
    tags = {k: raw_tags[k] for k in sorted(raw_tags, key=raw_tags.get, reverse=True)}
    return render(request, "blog/blog_home.html", {'blogs': blogs, 'tags': tags})


class BlogListView(ListView):
    model = Blog
    paginate_by = 3
    template_name = "blog/blog_list.html"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = EditBlogForm
    model = Blog
    action = "Add"
    template_name = "blog/blog_form.html"


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    form_class = EditBlogForm
    model = Blog
    action = "Edit"
    template_name = "blog/blog_form.html"


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
