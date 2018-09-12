from stats import *
from random import *


inventory_useby_hand = [steal_gauntlet, golden_stick, bronze_shield]
inventory = [inventory_useby_hand]
inventory_player_userby_hand = []
inventory_orc_useby_hand = []
all_index = ["HP", "STR", "DEF", "LUCK", "AGI"]

def tang_index(item_wear, name_wear):
    for i in all_index:
        name_wear[i] += item_wear[i]

def giam_index(item_undress, name_undress):
    for i in all_index:
        name_undress[i] -= item_undress[i]

def un_dress(item_undress, name_undress):
    giam_index(item_undress, name_undress)
    if name_undress == player:
        inventory_player_userby_hand.clear()
        giam_index(item_undress, name_undress)
    elif name_undress == Orc:
        inventory_player_userby_hand.clear()
        giam_index(item_undress, name_undress)

def wear(item_wear, name_wear):
    tang_index(item_wear, name_wear)
    if name_wear == player:
        inventory_player_userby_hand.append(item_wear)
        tang_index(item_wear, name_wear)
    elif name_wear == Orc:
        inventory_player_userby_hand.append(item_wear)
        tang_index(item_wear, name_wear)

    print('Chỉ số hiện tại của', name_wear["NAME"])

def use_item(name_use_item):
    useby = choice(inventory)
    item_use = choice(useby)
    if name_use_item == player:
        while True:
            print("Bạn nhặt được", item_use["NAME"])
            print("Bạn có mốn sử dụng", item_use["NAME"], "không")
            print("1. Có")
            print("2. Không")
            useitem_yes_or_no = input(">>>")
            if useitem_yes_or_no == "1":
                print("Bạn đã sử dụng", item_use["NAME"])
                if useby == inventory_useby_hand:
                    for undress in inventory_player_userby_hand:
                        un_dress(item_use, name_use_item)
                    wear(item_use, name_use_item)
                break
            elif useitem_yes_or_no == "2":
                print("Bạn đã vứt đồ đi")
                break
            else:
                print("Bạn chỉ được nhập 1 hoặc 2")
                print("Nhập lại đi !!!")
    if name_use_item == Orc:
        print("Orc đã sử dụng", item_use["NAME"])
        if useby == inventory_useby_hand:
            for undress in inventory_orc_useby_hand:
                un_dress(undress, name_use_item)
            wear(useby, name_use_item)


