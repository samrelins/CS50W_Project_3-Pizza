from .models import *

dishes = ["Regular Pizza", "Sicilian Pizza", "Pasta", "Salads", "Dinner Platters"]
Salad_items = ["Garden Salad", 625, "Greek Salad", 825, "Antipasto", 825, "Salad w/Tuna", 825]
dinner_items = ["Garden Salad", 3500, 6000, "Greek Salad", 4500, 7000, "Antipasto", 4500, 7000, "Baked Ziti", 3500, 6000, "Meatball Parm", 4500, 7000, "Chicken Parm", 4500, 8000]
pasta_items = ["Baked Ziti w/Mozzarella", 650, "Baked Ziti w/Meatballs", 875, "Baked Ziti w/Chicken", 975]
sub_items = ["Cheese", 650, 795, "Italian", 650, 795, "Ham + Cheese", 650, 795, "Meatball", 650, 795, "Tuna", 650, 795, "Turkey", 750, 850, "Chicken Parmigiana", 750, 850, "Eggplant Parmigiana", 650, 795, "Steak", 650, 795, "Steak + Cheese", 695, 850, "Hamburger", 460, 695, "Cheeseburger", 510, 745, "Fried Chicken", 695, 850, "Veggie", 695, 850]
sicilian_items = ["Cheese", 2345, 3770, "1 item", 2545, 3970, "2 items", 2745, 4170, "3 items", 2845, 4370, "Special", 2945, 4470]
regular_items = ["Cheese", 1220, 1745, "1 topping", 1320, 1945, "2 toppings", 1470, 2145, "3 toppings", 1570,	2345, "Special", 1725, 2545]

toppings = ["Pepperoni", "Sausage", "Mushrooms", "Onions", "Ham", "Canadian Bacon", "Pineapple", "Eggplant", "Tomato & Basil", "Green Peppers", "Hamburger", "Spinach", "Artichoke", "Buffalo Chicken", "Barbecue Chicken", "Anchovies", "Black Olives", "Fresh Garlic", "Zucchini"]

def addstuff():

    #salad = MenuDish.objects.get(pk=5)
    #for item in Salad_items:
        #if Salad_items.index(item) % 2 == 0:
            #salad_item = MenuItem(name=item, dish=salad)
            #salad_item.save()
        #else:
            #salad_item.large_price = item
            #salad_item.save()


    #pasta = MenuDish.objects.get(pk=4)
    #for item in pasta_items:
        #if pasta_items.index(item) % 2 == 0:
            #pasta_item = MenuItem(name=item, dish=pasta)
            #pasta_item.save()
        #else:
            #pasta_item.large_price = item
            #pasta_item.save()


    #dinner = MenuDish.objects.get(pk=6)
    #for item in dinner_items:
        #if dinner_items.index(item) % 3 == 0:
            #dinner_item = MenuItem(name=item, dish=dinner)
            #dinner_item.save()
        #elif dinner_items.index(item) % 2 == 0:
            #dinner_item.large_price = item
            #dinner_item.save()
        #else:
            #dinner_item.small_price = item
            #dinner_item.save()


    #sub = MenuDish.objects.get(pk=1)
    #for item in sub_items:
        #if sub_items.index(item) % 3 == 0:
            #sub_item = MenuItem(name=item, dish=sub)
            #sub_item.save()
        #elif sub_items.index(item) % 2 == 0:
            #sub_item.large_price = item
            #sub_item.save()
        #else:
            #sub_item.small_price = item
            #sub_item.save()


    #sicilian = MenuDish.objects.get(pk=2)
    #for item in sicilian_items:
        #if sicilian_items.index(item) % 3 == 0:
            #sicilian_item = MenuItem(name=item, dish=sicilian)
            #sicilian_item.save()
        #elif sicilian_items.index(item) % 2 == 0:
            #sicilian_item.large_price = item
            #sicilian_item.save()
        #else:
            #sicilian_item.small_price = item
            #sicilian_item.save()


    #regular = MenuDish.objects.get(pk=3)
    #for item in regular_items:
        #if regular_items.index(item) % 3 == 0:
            #regular_item = MenuItem(name=item, dish=regular)
            #regular_item.save()
        #elif regular_items.index(item) % 2 == 0:
            #regular_item.large_price = item
            #regular_item.save()
        #else:
            #regular_item.small_price = item
            #regular_item.save()
    #salad = MenuDish.objects.get(pk=5)

    for item in toppings:
        topping = MenuExtra(name=item)
        topping.save()
