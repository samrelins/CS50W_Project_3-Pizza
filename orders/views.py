from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def auth_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("login", {"message": "Invalid login details"})
    if request.method == "GET":
        return render(request, "orders/login.html", {"messgage": None})


def auth_register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username, email, password)

        login(request, user)

        return redirect("index")

    if request.method == "GET":
        return render(request, "orders/register.html", {"messgage": None})


def index(request):
    items = MenuItem.objects.all()
    dishes = MenuDish.objects.all()
    context = {
            "items": items,
            "dishes": dishes
    }
    return render(request, "orders/index.html", context)

def orders(request):
    return render(request, "orders/orders.html")


def new_order(request): #will need an order id input at some point
    return render(request, "orders/new_order.html")


def add_item(request):
    items = MenuItem.objects.all()
    dishes = MenuDish.objects.all()
    context = {
            "items": items,
            "dishes": dishes
    }
    return render(request, "orders/add_item.html", context)


def item_options(request, item_id):
    try:
        item = MenuItem.objects.get(pk=item_id)
    except MenuItem.DoesNotExist:
        raise Http404("Menu item doesn't exist")

    if item.dish.one_size and len(item.list_extras()) == 0:
        return redirect("add_item")

    context = {
            "item": item,
            "extras": item.list_extras(),
            "extras_allowed": range(0,item.extras_allowed)
    }
    return render(request, "orders/item_options.html", context)


def complete_order(request):
    return render(request, "orders/complete_order.html")


def review_order(request):
    return render(request, "orders/review_order.html")

