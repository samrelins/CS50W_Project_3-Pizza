from django.test import Client, TestCase
from django.contrib.auth.models import User
from orders.models import *

# Create your tests here.

class OrdersTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='test_user', password='password')
        order = Order.objects.create(user=user)
        d = MenuDish.objects.create(name="dish")
        mi1 =  MenuItem.objects.create(name="plate", dish=d)
        i1 = OrderItem.objects.create(item=mi1)


    def test_orders_page(self):
        user = User.objects.get(username='test_user')
        c = Client()
        c.force_login(user)
        response = c.get("/orders/")
        self.assertEqual(response.status_code, 200)


    def test_order_page(self):
        user = User.objects.get(username='test_user')
        order = Order.objects.get(user=user)
        c = Client()
        c.force_login(user)
        response = c.get(f"/orders/{order.id}")
        self.assertEqual(response.status_code, 200)


    def test_new_order(self):
        user = User.objects.get(username='test_user')
        order = Order.objects.get(user=user)
        c = Client()
        c.force_login(user)

        response = c.get(f"/orders/new", follow=True)
        self.assertEqual(response.redirect_chain, [('/orders/1', 302)])

        order.paid = True;
        order.save()
        response = c.get(f"/orders/new", follow=True)
        self.assertEqual(response.redirect_chain, [('/orders/2', 302)])


    def test_choose_item(self):
        user = User.objects.get(username='test_user')
        order = Order.objects.get(user=user)
        c = Client()
        c.force_login(user)
        response = c.get(f"/orders/choose_item")
        self.assertEqual(response.status_code, 200)

        order.paid = True;
        order.save()
        response = c.get(f"/orders/choose_item", follow=True)
        self.assertEqual(response.redirect_chain, [('/orders/', 302)])


    def test_order_payment(self):
        user = User.objects.get(username='test_user')
        order = Order.objects.get(user=user)
        c = Client()
        c.force_login(user)
        print("checking pay route without items in order")
        response = c.post(f"/orders/pay", follow=True)
        self.assertEqual(response.redirect_chain, [('/orders/1', 302)])

        item = OrderItem.objects.get(id=1)
        order.items.add(item)
        print("checking pay route with items in order")
        response = c.post(f"/orders/pay", follow=True)
        order = Order.objects.get(user=user)
        self.assertTrue(order.paid)
        self.assertEqual(response.redirect_chain, [('/orders/', 302)])

