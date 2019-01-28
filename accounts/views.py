from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def auth_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect("kitchen_menu")

            return redirect("menu")
        else:
            return redirect("login", {"message": "Invalid login details"})
    if request.method == "GET":
        return render(request, "accounts/login.html", {"messgage": None})


def auth_register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username, email, password)

        login(request, user)

        return redirect("menu")

    if request.method == "GET":
        return render(request, "accounts/register.html", {"messgage": None})


def auth_logout(request):
    is_staff = request.user.is_staff
    logout(request)
    if is_staff:
        return redirect("login")
    else:
        return redirect("menu")


