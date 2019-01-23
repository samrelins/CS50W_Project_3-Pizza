from django.shortcuts import render, redirect
from menu.models import *
from orders.models import *

# Create your views here.
def kitchen_menu(request):
    if not request.user.is_staff:
        return redirect("login")

    items = MenuItem.objects.all()
    dishes = MenuDish.objects.all()
    context = {
            "items": items,
            "dishes": dishes
    }
    return render(request, "kitchen/menu.html", context)


def open_orders(request):
    if not request.user.is_staff:
        return redirect("login")

    orders = Order.objects.filter(paid=True, complete=False).all()

    context = {
            "orders": orders
    }
    return render(request, "kitchen/open_orders.html", context)


def historic_orders(request):
    if not request.user.is_staff:
        return redirect("login")

    orders = Order.objects.filter(paid=True, complete=True).all()

    context = {
            "orders": orders
    }
    return render(request, "kitchen/historic_orders.html", context)

def kitchen_order(request, order_id):
    if not request.user.is_staff:
        return redirect("login")

    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404("Order doesn't exist")

    context = {
            "order": order,
    }

    if order.complete:
        return render(request, "kitchen/historic_order.html", context)
    elif order.paid:
        return render(request, "kitchen/open_order.html", context)
    else:
        return redirect("open_orders")

def complete_order(request, order_id):
    if not request.user.is_staff:
        return redirect("login")

    if request.method == "POST":
        print("completing order")
        completed_order = Order.objects.get(pk=order_id)
        print(completed_order)
        completed_order.complete = True
        print(completed_order.complete)
        completed_order.save()
        return redirect("open_orders")

    else:
        return redirect("open_orders")
