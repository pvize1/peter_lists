from django.shortcuts import render
from django.contrib import messages
from random import choice

# Create your views here.
def PasswdHome(request):
    return render(request, "passwd/passwd_home.html")


def PasswdDisplay(request):
    chars = list("abcdefghijklmnopqrstuvwxyz")
    generated_password = choice(chars)

    len_text = request.GET.get("length", 12)
    msg_text = "Password generated with length: " + len_text
    messages.add_message(request, messages.INFO, msg_text)
    msg_text = ""

    if request.GET.get("uppercase"):
        chars.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        msg_text = "With uppercase characters; "
    if request.GET.get("special"):
        chars.extend(list("!£$%^&*()_+@#[]{}=-?,.<>"))
        msg_text = msg_text + "With special characters; "
    if request.GET.get("numbers"):
        chars.extend(list("1234567890"))
        msg_text = msg_text + "With numbers"

    messages.add_message(request, messages.INFO, msg_text)

    for i in range(int(len_text) - 1):
        generated_password += choice(chars)

    return render(
        request, "passwd/passwd_display.html", {"password": generated_password}
    )
