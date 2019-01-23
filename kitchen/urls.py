from django.urls import path

from . import views

urlpatterns = [
    path("", views.kitchen_menu, name="kitchen_menu"),
    path("open", views.open_orders, name="open_orders"),
    path("historic", views.historic_orders, name="historic_orders"),
    path("<int:order_id>", views.kitchen_order, name="kitchen_order"),
    path("complete_order/<int:order_id>", views.complete_order, name="complete_order"),
]
