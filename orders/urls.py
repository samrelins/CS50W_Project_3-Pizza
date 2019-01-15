from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.auth_login, name="login"),
    path("register", views.auth_register, name="register"),
    path("logout", views.auth_logout, name="logout"),
    path("orders", views.orders, name="orders"),
    path("order/<int:order_id>", views.order, name="order"),
    path("add_item", views.add_item, name="add_item"),
    path("item_options/<int:item_id>", views.item_options, name="item_options"),
    path("complete_order", views.complete_order, name="complete_order"),
    path("review_order", views.review_order, name="review_order")
]
