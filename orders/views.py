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
            return redirect("orders")
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


def auth_logout(request):
    logout(request)
    return redirect("index")


def index(request):
    items = MenuItem.objects.all()
    dishes = MenuDish.objects.all()
    context = {
            "items": items,
            "dishes": dishes
    }
    return render(request, "orders/index.html", context)


def orders(request):
    if not request.user.is_authenticated:
        return redirect("login")

    pending_order = Order.objects.filter(user=request.user, paid="False").first()
    historic_orders = Order.objects.filter(user=request.user, paid="True").all()
    context = {
            "historic_orders": historic_orders,
            "pending_order": pending_order
    }
    return render(request, "orders/orders.html", context)


def order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404("Order doesn't exist")

    context = {
            "order": order,
    }
    return render(request, "orders/order.html", context)


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

    if item.extras_limit:
        extras_allowed = range(0,item.extras_allowed)
    else:
        extras_allowed = 0

    context = {
            "item": item,
            "extras": item.list_extras(),
            "extras_allowed": extras_allowed
    }
    return render(request, "orders/item_options.html", context)


def complete_order(request):
    return render(request, "orders/complete_order.html")


def review_order(request):
    return render(request, "orders/review_order.html")

