from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path(route="", view=views.BlogHome, name="home"),
    path(route="list/", view=views.BlogListView.as_view(), name="list"),
    path(route="list/tag/<tag_name>", view=views.BlogTagListView.as_view(), name="tag_list"),
    path(route="tags/", view=views.BlogAllTagsView, name="all_tags"),
    path(route="detail/<int:pk>/", view=views.BlogDetailView.as_view(), name="detail"),

    path(route="add/", view=views.BlogCreateView.as_view(), name="add"),
    path(route="update/<int:pk>/", view=views.BlogUpdateView.as_view(), name="update"),
    path(route="delete/<int:pk>/", view=views.BlogDeleteView.as_view(), name="delete"),
]
