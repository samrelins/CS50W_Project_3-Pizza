from django.contrib import admin

from .models import *

# Register your models here.
class MenuExtraAdmin(admin.ModelAdmin):
    filter_horizontal = ("items","dishes",)

admin.site.register(MenuDish)
admin.site.register(MenuItem)
admin.site.register(MenuExtra, MenuExtraAdmin)
