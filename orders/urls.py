from django.urls import path

from . import views

urlpatterns = [
    path("", views.orders, name="orders"),
    path("new", views.new_order, name="new_order"),
    path("<int:order_id>", views.order, name="order"),
    path("choose_item", views.choose_item, name="choose_item"),
    path("item_options/<int:item_id>", views.item_options, name="item_options"),
    path("add_item", views.add_item, name="add_item"),
    path("edit_item/<int:item_id>", views.edit_item, name="edit_item"),
    path("remove_item/<int:item_id>", views.remove_item, name="remove_item"),
    path("pay", views.order_payment, name="order_payment")
]
