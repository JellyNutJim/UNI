from items import *
from map import rooms

def get_room():
    return current_room

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]
