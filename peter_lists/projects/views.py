from django.shortcuts import render

# Create your views here.
def ProjHomeView(request):
    return render(request, "projects/home.html")


def ProjAdminView(request):
    return render(request, "projects/home.html")
