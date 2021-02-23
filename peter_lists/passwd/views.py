from django.shortcuts import render
from django.http import HttpResponse
from random import choice

# Create your views here.
def home(request):
    return render(request, "passwd/passwd_home.html")


def display(request):
    chars = list("abcdefghijklmnopqrstuvwxyz")
    generated_password = choice(chars)

    if request.GET.get("uppercase"):
        chars.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("special"):
        chars.extend(list("!£$%^&*()_+@#[]{}=-\/?,.<>"))
    if request.GET.get("numbers"):
        chars.extend(list("1234567890"))
    length = int(request.GET.get("length", 12))

    for i in range(length - 1):
        generated_password += choice(chars)

    return render(
        request, "passwd/passwd_display.html", {"password": generated_password}
    )


def simple_text(request):
    return HttpResponse("<h1>Empty</h1>")
