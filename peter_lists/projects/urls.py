from django.urls import path
from . import views

app_name = "projects"
urlpatterns = [
    path(route="admin", view=views.ProjAdminView, name="proj_admin"),
]
