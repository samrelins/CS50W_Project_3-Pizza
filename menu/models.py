from django.db import models

# Create your models here.
class MenuDish(models.Model):
    name = models.CharField(max_length=64)
    extra_price = models.IntegerField(default=0)
    one_size = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    def print_extra_price(self):
        price = "$" + str("{:.2f}".format(self.extra_price/100))
        return price

class MenuItem(models.Model):
    name = models.CharField(max_length=64)
    dish = models.ForeignKey(MenuDish, on_delete=models.CASCADE, related_name="items")
    small_price = models.IntegerField(null=True, blank=True)
    large_price = models.IntegerField(default=0)
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

        if len(extras) == 0:
            return 0
        else:
            return extras


class MenuExtra(models.Model):
    name = models.CharField(max_length=64)
    dishes = models.ManyToManyField(MenuDish, related_name="extras", blank=True)
    items = models.ManyToManyField(MenuItem, related_name="extras", blank=True)

    def __str__(self):
        return f"Extra: {self.name}"


