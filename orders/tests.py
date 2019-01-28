from django.test import Client, TestCase
from django.contrib.auth.models import User
from orders.models import *

# Create your tests here.

class OrdersTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='test_user', password='password')
        order = Order.objects.create(user=user)


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


