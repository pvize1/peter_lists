from django.urls import path
from . import views

app_name = "projects"
urlpatterns = [
    path(route="", view=views.ProjHomeView, name="proj_home"),
    path(route="admin", view=views.ProjAdminView, name="proj_admin"),
]
