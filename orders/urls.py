from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.auth_login, name="login"),
    path("register", views.auth_register, name="register"),
    path("orders", views.orders, name="orders"),
    path("add_item", views.add_item, name="add_item"),
    path("item_options/<int:item_id>", views.item_options, name="item_options"),
    path("new_order", views.new_order, name="new_order"),
    path("complete_order", views.complete_order, name="complete_order"),
    path("review_order", views.review_order, name="review_order")
]
