from django.shortcuts import render

# Create your views here.
def BlogHome(request):
    return render(request, "blog/blog_home.html")
