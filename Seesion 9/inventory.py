steal_gauntlet = {
    "NAME": "Steal gauntlet",
    "HP": 0,
    "STR": 5,
    "DEF": 5,
    "LUCK": 0,
    "AGI": 3,
}

bronze_shield = {
    "NAME": "Bronze shield",
    "HP": 0,
    "STR": 4,
    "DEF": 12,
    "LUCK": 0,
    "AGI": -5,
}

golden_stick = {
    "NAME": "Golden stick",
    "HP": 20,
    "STR": 100,
    "DEF": 0,
    "LUCK": 0,
    "AGI": 15,
}


from life_of_TechKids import *
from random import *
from combat import *

inventory_useby_hand = [steal_gauntlet, golden_stick, bronze_shield]
inventory = [inventory_useby_hand]
inventory_player_userby_hand = []
inventory_orc_useby_hand = []

def un_dress(item_undress, name_undress):
    name_undress["HP", "STR", "DEF", "LUCK", "AGI"] -= item_undress["HP", "STR", "DEF", "LUCK", "AGI"]
    if name_undress == player:
        inventory_player_userby_hand.clear()
    elif name_undress == Orc:
        inventory_player_userby_hand.clear()

def wear(item_wear, name_wear):
    name_wear["HP", "STR", "DEF", "LUCK", "AGI"] -= item_wear["HP", "STR", "DEF", "LUCK", "AGI"]
    if name_wear == player:
        inventory_player_userby_hand.append(item_wear)
    elif name_wear == Orc:
        inventory_player_userby_hand.append(item_wear)

    print('Chỉ số hiện tại của', name_wear)
    show_index(name_wear)

def use_item(name_use_item):
    useby = choice(inventory)
    if name_use_item == player:
        if useby == inventory_useby_hand:
            for undress in inventory_player_userby_hand:
                un_dress(undress, name_use_item)
            wear(useby, name_use_item)
    if name_use_item == Orc:
        if useby == inventory_useby_hand:
            for undress in inventory_orc_useby_hand:
                un_dress(undress, name_use_item)
            wear(useby, name_use_item)
