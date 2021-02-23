from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "passwd/passwd_home.html")

def display(request):
    generated_password="Testing"
    return render(request, "passwd/passwd_display.html", {"password": generated_password})

def simple_text(request):
    return HttpResponse("<h1>Empty</h1>")
