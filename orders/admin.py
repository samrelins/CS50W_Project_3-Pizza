from django.contrib import admin

from .models import *

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ("items",)

class OrderItemAdmin(admin.ModelAdmin):
    filter_horizontal = ("extras",)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
