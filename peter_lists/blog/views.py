from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import Trim, Lower
from django.urls import reverse_lazy
from .models import Blog
from .forms import EditBlogForm


def tag_count(topn=0):
    # TODO Move to model manager
    raw_tags = (
        Blog.blog.order_by("tag")
        .values("tag")
        .annotate(count=Count("tag"), tag_new=Trim(Lower("tag")))
    )
    count_tags = dict()
    for record in raw_tags:
        for tag in record["tag_new"].split(","):
            k = tag.strip()
            if len(k) > 0:
                count_tags[k] = count_tags.get(k, 0) + record["count"]
    # TODO Sort by key after value, for common values
    if topn == 0:
        return {
            k: count_tags[k]
            for k in sorted(count_tags, key=count_tags.get, reverse=True)
        }
    else:
        return {
            k: count_tags[k]
            for k in sorted(count_tags, key=count_tags.get, reverse=True)[:topn]
        }


# Create your views here.
def BlogHome(request):
    blogs = Blog.blog.filter(user=request.user).order_by("-modified")[:3]
    blog_count = blogs.count()
    tag_sorted = tag_count(topn=5)
    return render(request, "blog/blog_home.html", {"blogs": blogs, "tags": tag_sorted, "blog_count": blog_count})


class BlogListView(PermissionRequiredMixin, ListView):
    model = Blog
    paginate_by = 3
    template_name = "blog/blog_list.html"
    permission_required = "blog.view_blog"


def BlogAllTagsView(request):
    tag_sorted = tag_count()
    return render(request, "blog/blog_tags.html", {"tags": tag_sorted})
    # TODO turn into ListView with paginate


class BlogTagListView(PermissionRequiredMixin, ListView):
    model = Blog
    paginate_by = 3
    template_name = "blog/blog_list.html"
    permission_required = "blog.view_blog"

    def get_queryset(self):
        return Blog.blog.filter(tag__contains=self.kwargs["tag_name"])


class BlogDetailView(PermissionRequiredMixin, DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    permission_required = "blog.view_blog"


class BlogCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = EditBlogForm
    model = Blog
    action = "Add"
    template_name = "blog/blog_form.html"
    permission_required = "blog.add_blog"


class BlogUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    form_class = EditBlogForm
    model = Blog
    action = "Edit"
    template_name = "blog/blog_form.html"
    permission_required = "blog.change_blog"


class BlogDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:list")
    permission_required = "blog.delete_blog"
