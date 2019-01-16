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
            return redirect("/")
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


def new_order(request):
    if not request.user.is_authenticated:
        return redirect("login")

    unpaid_order = Order.objects.filter(user=request.user, paid="False").first()

    if unpaid_order:
        return redirect(f"order/{unpaid_order.id}")

    order = Order(user=request.user)
    order.save()

    return redirect(f"order/{order.id}")


def orders(request):
    if not request.user.is_authenticated:
        return redirect("login")

    orders = Order.objects.filter(user=request.user).all()

    pending_order = orders.filter(paid="False").first()
    historic_orders = orders.filter(paid="True").order_by("-date")
    context = {
            "historic_orders": historic_orders,
            "pending_order": pending_order
    }
    return render(request, "orders/orders.html", context)


def order(request, order_id):
    if not request.user.is_authenticated:
        return redirect("login")

    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404("Order doesn't exist")

    context = {
            "order": order,
    }

    if order.paid:
        return render(request, "orders/historic_order.html", context)
    else:
        return render(request, "orders/new_order.html", context)




def choose_item(request):
    if not request.user.is_authenticated:
        return redirect("login")

    items = MenuItem.objects.all()
    dishes = MenuDish.objects.all()
    context = {
            "items": items,
            "dishes": dishes
    }
    return render(request, "orders/choose_item.html", context)


def item_options(request, item_id):
    if not request.user.is_authenticated:
        return redirect("login")

    try:
        item = MenuItem.objects.get(pk=item_id)
    except MenuItem.DoesNotExist:
        raise Http404("Menu item doesn't exist")

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


def add_item(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        print(request.POST)
        item_id = request.POST.get('item_id')
        extra_ids = request.POST.getlist('extras')
        size = request.POST.get("size")

        menu_item = MenuItem.objects.get(pk=item_id)
        order_item = OrderItem(item=menu_item)

        print(size)
        if size == "small":
            order_item.small = True

        order_item.save()

        for id in extra_ids:
            extra = MenuExtra.objects.get(pk=id)
            order_item.extras.add(extra)

        order_item.save()

        current_order = Order.objects.get(user=request.user, paid="False")
        current_order.items.add(order_item)
        current_order.save()
        return redirect(f"order/{current_order.id}")


def complete_order(request):
    if not request.user.is_authenticated:
        return redirect("login")

    current_order = Order.objects.get(user=request.user, paid="False")

    if request.method == "POST":
        current_order.paid = True
        current_order.save()
        return redirect("orders")

    else:
        context = {
                "order": current_order,
        }
        return render(request, "orders/complete_order.html", context)


def review_order(request):
    return render(request, "orders/review_order.html")

