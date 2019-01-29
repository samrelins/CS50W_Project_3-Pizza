# automatically loads Pinochio's menu into database
#    run using shell in django:
#    i.e. $ python manage.py < menu/loadmenu.py

from menu.load_menu import *
from accounts.load_su import *

load_menu()
load_su()
