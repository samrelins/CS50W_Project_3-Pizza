# function (a crude one!) that loads Pinochio's menu into database
#    used in menu.tests.py and pizza.load_db.py

from menu.models import *

dishes = ["Regular Pizza", "Sicilian Pizza", "Subs", "Pasta", "Salads", "Dinner Platters"]

regular_items = ["Cheese", 1220, 1745, 
                    "1 topping", 1320, 1945, 
                    "2 toppings", 1470, 2145, 
                    "3 toppings", 1570,	2345, 
                    "Special", 1725, 2545]

sicilian_items = ["Cheese", 2345, 3770, 
                    "1 item", 2545, 3970, 
                    "2 items", 2745, 4170, 
                    "3 items", 2845, 4370, 
                    "Special", 2945, 4470]

sub_items = ["Cheese", 650, 795, 
                "Italian", 650, 795, 
                "Ham + Cheese", 650, 795, 
                "Meatball", 650, 795, 
                "Tuna", 650, 795, 
                "Turkey", 750, 850, 
                "Chicken Parmigiana", 750, 850, 
                "Eggplant Parmigiana", 650, 795, 
                "Steak", 650, 795, 
                "Steak + Cheese", 695, 850, 
                "Hamburger", 460, 695, 
                "Cheeseburger", 510, 745, 
                "Fried Chicken", 695, 850, 
                "Veggie", 695, 850]

pasta_items = ["Baked Ziti w/Mozzarella", 650, 
                "Baked Ziti w/Meatballs", 875, 
                "Baked Ziti w/Chicken", 975]

Salad_items = ["Garden Salad", 625, 
                "Greek Salad", 825, 
                "Antipasto", 825, 
                "Salad w/Tuna", 825]

dinner_items = ["Garden Salad", 3500, 6000, 
                "Greek Salad", 4500, 7000, 
                "Antipasto", 4500, 7000, 
                "Baked Ziti", 3500, 6000, 
                "Meatball Parm", 4500, 7000, 
                "Chicken Parm", 4500, 8000]

toppings = ["Pepperoni", "Sausage", "Mushrooms", 
            "Onions", "Ham", "Canadian Bacon", 
            "Pineapple", "Eggplant", "Tomato & Basil", 
            "Green Peppers", "Hamburger", "Spinach", 
            "Artichoke", "Buffalo Chicken", "Barbecue Chicken", 
            "Anchovies", "Black Olives", "Fresh Garlic", "Zucchini"]

def load_menu():
    for dish in dishes:
        dish = MenuDish(name=dish)
        dish.save()

    regular = MenuDish.objects.filter(name="Regular Pizza").first()
    regular.one_size = False
    regular.save()

    for n, item in enumerate(regular_items):
        if (n + 1) % 3 == 1:
            regular_item = MenuItem(name=item, dish=regular)
            regular_item.save()
        elif (n + 1) % 3 == 0:
            regular_item.large_price = item
            regular_item.save()
        elif (n + 1) % 3 == 2:
            regular_item.small_price = item
            regular_item.save()


    regular_pizzas = MenuItem.objects.filter(dish=regular)
    for n, pizza in enumerate(regular_pizzas):
        pizza.extras_limit = True
        pizza.extras_allowed = n
        pizza.save()


    sicilian = MenuDish.objects.filter(name="Sicilian Pizza").first()
    sicilian.one_size = False
    sicilian.save()
    for n, item in enumerate(sicilian_items):
        if (n + 1) % 3 == 1:
            sicilian_item = MenuItem(name=item, dish=sicilian)
            sicilian_item.save()
        elif (n + 1) % 3 == 0:
            sicilian_item.large_price = item
            sicilian_item.save()
        elif (n + 1) % 3 == 2:
            sicilian_item.small_price = item
            sicilian_item.save()


    sicilian_pizzas = MenuItem.objects.filter(dish=sicilian)
    for n, pizza in enumerate(sicilian_pizzas):
        pizza.extras_limit = True
        pizza.extras_allowed = n
        pizza.save()


    sub = MenuDish.objects.filter(name="Subs").first()
    sub.extra_price = 50
    sub.one_size = False
    sub.save()

    for n, item in enumerate(sub_items):
        if  (n + 1) % 3 == 0:
            sub_item.large_price = item
            sub_item.save()
        elif (n + 1) % 3 == 1:
            sub_item = MenuItem(name=item, dish=sub)
            sub_item.save()
        elif (n + 1) % 3 == 2:
            sub_item.small_price = item
            sub_item.save()

    spo_sub = MenuItem.objects.create(name="Sausage, Peppers & Onions", dish=sub, large_price=850)
    spo_sub.save()

    pasta = MenuDish.objects.filter(name="Pasta").first()
    for n, item in enumerate(pasta_items):
        if n % 2 == 0:
            pasta_item = MenuItem(name=item, dish=pasta)
            pasta_item.save()
        else:
            pasta_item.large_price = item
            pasta_item.save()


    salad = MenuDish.objects.filter(name="Salads").first()
    for n, item in enumerate(Salad_items):
        if n % 2 == 0:
            salad_item = MenuItem(name=item, dish=salad)
            salad_item.save()
        else:
            salad_item.large_price = item
            salad_item.save()


    dinner = MenuDish.objects.filter(name="Dinner Platters").first()
    dinner.one_size = False
    dinner.save()
    for n, item in enumerate(dinner_items):
        if (n + 1) % 3 == 1:
            dinner_item = MenuItem(name=item, dish=dinner)
            dinner_item.save()
        elif (n + 1) % 3 == 0:
            dinner_item.large_price = item
            dinner_item.save()
        elif (n + 1) % 3 == 2:
            dinner_item.small_price = item
            dinner_item.save()


    for item in toppings:
        topping = MenuExtra(name=item)
        topping.save()
        topping.dishes.add(regular, sicilian)

    extra_cheese = MenuExtra.objects.create(name="Extra Cheese")
    extra_cheese.save()
    extra_cheese.dishes.add(sub)

    steak_sub = MenuItem.objects.get(name="Steak + Cheese")
    onions = MenuExtra.objects.get(name="Onions")
    green_peppers = MenuExtra.objects.get(name="Green Peppers")
    mushrooms = MenuExtra.objects.get(name="Mushrooms")
    s_toppings = [onions, green_peppers, mushrooms]

    for topping in s_toppings:
        topping.items.add(steak_sub)


if __name__ == "__main__":
    load_menu()

