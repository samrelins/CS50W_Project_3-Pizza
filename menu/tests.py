from django.test import TestCase
from menu.models import *
from menu.load_menu import *

# Create your tests here.

class OrdersTestCase(TestCase):

    def setUp(self):
        load_menu()


    def test_menu_dishes(self):
        self.assertEqual(len(MenuDish.objects.all()), 6)
