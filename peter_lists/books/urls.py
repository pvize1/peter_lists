from django.urls import path
from . import views

app_name = "books"
urlpatterns = [path(route='', view=views.BookListView.as_view(), name='list'),
               path(route ='<slug:slug>/', view=views.BookDetailView.as_view(), name="detail"), ]
