from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

@login_required
def orders(request):

    orders = Order.objects.filter(user=request.user).all()

    pending_order = orders.filter(paid="False").first()
    historic_orders = orders.filter(paid="True").order_by("-date")
    context = {
            "historic_orders": historic_orders,
            "pending_order": pending_order
    }
    return render(request, "orders/orders.html", context)


@login_required
def new_order(request):

    unpaid_order = Order.objects.filter(user=request.user, paid="False").first()

    if unpaid_order:
        return redirect("order", order_id=unpaid_order.id)

    order = Order(user=request.user)
    order.save()

    return redirect("order", order_id=order.id)


@login_required
def order(request, order_id):

    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404("Order doesn't exist")

    if not order.user == request.user:
        return redirect("orders")

    context = {
            "order": order,
    }

    if order.paid:
        return render(request, "orders/historic_order.html", context)
    else:
        return render(request, "orders/new_order.html", context)


@login_required
def choose_item(request):

    unpaid_order = Order.objects.filter(user=request.user, paid="False").first()

    if not unpaid_order:
        return redirect("orders")

    items = MenuItem.objects.all()
    dishes = MenuDish.objects.all()
    context = {
            "items": items,
            "dishes": dishes
    }
    return render(request, "orders/choose_item.html", context)


@login_required
def item_options(request, item_id):

    unpaid_order = Order.objects.filter(user=request.user, paid="False").first()

    if not unpaid_order:
        return redirect("orders")

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


@login_required
def add_item(request):

    if request.method == "POST":
        item_id = request.POST.get('item_id')
        extra_ids = request.POST.getlist('extras')
        size = request.POST.get("size")

        menu_item = MenuItem.objects.get(pk=item_id)
        order_item = OrderItem(item=menu_item)

        for id in extra_ids:
            try:
                id = int(id)
            except:
                return redirect("item_options", item_id=menu_item.id)

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
        return redirect("order", order_id=current_order.id)


@login_required
def edit_item(request, item_id):

    order_item = OrderItem.objects.get(pk=item_id)
    menu_item = order_item.item
    order_item.delete()
    return redirect("item_options", item_id=menu_item.id)


@login_required
def remove_item(request, item_id):

    order_item = OrderItem.objects.get(pk=item_id)
    order_item.delete()
    current_order = Order.objects.get(user=request.user, paid="False")
    return redirect("order", order_id=current_order.id)


@login_required
def order_payment(request):

    current_order = Order.objects.get(user=request.user, paid="False")

    if not current_order:
        return redirect("orders")
    else:
        if current_order.items_total() == 0:
            print("redirecting empty order")
            return redirect("order", order_id=current_order.id)

    if request.method == "POST":
        print("setting paid to true")
        current_order.paid = True
        current_order.save()
        return redirect("orders")
    else:
        context = {
                "order": current_order,
        }
        return render(request, "orders/order_payment.html", context)

