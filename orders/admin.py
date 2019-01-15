from django.contrib import admin

from .models import *

# Register your models here.

class MenuExtraAdmin(admin.ModelAdmin):
    filter_horizontal = ("items","dishes",)

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ("items",)

class OrderItemAdmin(admin.ModelAdmin):
    filter_horizontal = ("extras",)

admin.site.register(MenuDish)
admin.site.register(MenuItem)
admin.site.register(MenuExtra, MenuExtraAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
