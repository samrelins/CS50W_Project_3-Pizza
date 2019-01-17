from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from menu.models import *

# Create your models here.
class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    small = models.BooleanField(default=False)
    extras = models.ManyToManyField(MenuExtra, blank=True)

    def __str__(self): return f"Order Item: {self.item.dish} - {self.item.name}"

    def price(self):
        if self.small:
            item_price = self.item.small_price
        else:
            item_price = self.item.large_price

        if self.item.dish.extra_price:
            item_price += self.item.dish.extra_price * len(self.extras.all())

        return item_price

    def print_price(self):
        price = "$" + str("{:.2f}".format(self.price()/100))
        return price

class Order(models.Model):
    items = models.ManyToManyField(OrderItem, related_name="orders", blank=True)
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    date = models.DateTimeField(default=now, editable=False)
    paid = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Order Item: {self.user}"

    def total(self):

        order_total = 0
        for item in self.items.all():
            order_total += item.price()

        return order_total

    def print_total(self):
        total = "$" + str("{:.2f}".format(self.total()/100))
        return total

    def items_total(self):
        return len(self.items.all())

    def print_date(self):
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Nov", "Dec"]
        date = str(self.date.day)
        date += " " + months[self.date.month + 1]
        date += " " + str(self.date.year)
        return date

    def print_time(self):
        time = str(self.date.hour)
        if self.date.minute < 10:
            time += ":0" + str(self.date.minute)
        else:
            time += ":" + str(self.date.minute)
        return time



