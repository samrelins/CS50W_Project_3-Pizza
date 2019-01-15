from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class MenuDish(models.Model):
    name = models.CharField(max_length=64)
    extra_price = models.IntegerField()
    one_size = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class MenuItem(models.Model):
    name = models.CharField(max_length=64)
    dish = models.ForeignKey(MenuDish, on_delete=models.CASCADE, related_name="items")
    small_price = models.IntegerField(null=True, blank=True)
    large_price = models.IntegerField()
    extras_limit = models.BooleanField(default=False)
    extras_allowed = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.dish}: {self.name} - small: {self.print_small_price()}, large: {self.print_large_price()}"

    def print_small_price(self):
        if self.small_price:
            price = "$" + str("{:.2f}".format(self.small_price/100))
            return price
        else:
            return 1

    def print_large_price(self):
        if self.large_price:
            price = "$" + str("{:.2f}".format(self.large_price/100))
            return price
        else:
            return 1

    def list_extras(self):
        extras = []
        for extra in self.extras.all():
            extras.append(extra.name)
        for extra in self.dish.extras.all():
            extras.append(extra.name)
        return extras


class MenuExtra(models.Model):
    name = models.CharField(max_length=64)
    dishes = models.ManyToManyField(MenuDish, related_name="extras", blank=True)
    items = models.ManyToManyField(MenuItem, related_name="extras", blank=True)

    def __str__(self):
        return f"Extra: {self.name}"


class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    small = models.BooleanField(default=False)
    extras = models.ManyToManyField(MenuExtra, blank=True)

    def __str__(self):
        return f"Order Item: {self.item.dish} - {self.item.name}"

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

