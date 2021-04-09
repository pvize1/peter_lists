from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.db.models import Count
from django.urls import reverse_lazy
from .models import Blog
from .forms import EditBlogForm


# Create your views here.
def BlogHome(request):
    blogs = Blog.blog.order_by("-modified")[:3]
    raw_tags = (Blog.blog.values("tag")
                .annotate(count=Count("tag"))
                )
    count_tags = dict()
    for record in raw_tags:
        for tag in record['tag'].split(","):
            k = tag.strip().lower()
            count_tags[k] = count_tags.get(k, 0) + record['count']
    tag_sorted = {k: count_tags[k] for k in sorted(count_tags, key=count_tags.get, reverse=True)}
    return render(request, "blog/blog_home.html", {'blogs': blogs, 'tags': tag_sorted})


class BlogListView(ListView):
    model = Blog
    paginate_by = 3
    template_name = "blog/blog_list.html"


class BlogTagListView(ListView):
    model = Blog
    paginate_by = 3
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        return Blog.blog.filter(tag__contains=self.kwargs["tag_name"])


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
