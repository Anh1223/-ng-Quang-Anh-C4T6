from inventory import *
from random import *





def combat_round(attacker, defender):
    print(attacker["NAME"], "tấn công", defender["NAME"])
    calculate_crit(attacker)
    has_crit = calculate_crit(attacker)
    if has_crit:
        print("Đòn chí mạng")
        damage = attacker["STR"] * 2 - defender["DEF"]
    else:
        damage = attacker["STR"] - defender["DEF"]
    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "mất", damage, "HP")
        if attacker["HP"] < 0:
            attacker["HP"] = 0
        if defender["HP"] < 0:
            defender["HP"] = 0
        print(defender["NAME"], "còn", defender["HP"])
    else:
        attacker["HP"] -= abs(damage)
        print(attacker["NAME"], "mất", abs(damage), "HP")
        if attacker["HP"] < 0:
            attacker["HP"] = 0
        if defender["HP"] < 0:
            defender["HP"] = 0
        print(attacker["NAME"], "còn", attacker["HP"], "lost")

def combat_full(attacker, defender):
    auto_combat = True
    while True:
        combat_round(attacker, defender)
        show_index(attacker)
        show_index(defender)
        if defender["HP"] == 0:
            print(defender["NAME"], "die")
            use_item(attacker)
            show_index(attacker)
            break
        if attacker["HP"] == 0:
            print(attacker["NAME"], "đie")
            use_item(defender)
            show_index(defender)
            break

        combat_round(defender, attacker)
        show_index(defender)
        show_index(attacker)
        if attacker["HP"] == 0:
            print(attacker["NAME"], "đie")
            use_item(defender)
            show_index(defender)
            break
        if defender["HP"] == 0:
            print(defender["NAME"], "die")
            use_item(attacker)
            show_index(attacker)
            break

        if auto_combat:
            print("Bạn muốn:")
            print("1. Đánh tiếp")
            print("2. Chạy")
            print("3. Tự động đánh")
            option = input(">>>")
            if option == "1":
                print("Nhào Zô")
            elif option == "2":
                dice = randint(0, 100)
                if attacker["LUCK"] > dice:
                    print("Bạn đã chạy thoát")
                    break
                else:
                    print("Bạn đã chạy thoát không thành công")
            elif option == "3":
                auto_combat = False


def calculate_crit(name):
    has_crit = False
    dice = randint(0, 1000)
    chance = name["LUCK"] + name["AGI"]
    if chance > dice:
        has_crit = True
    return has_crit

def show_index(name_show_index):
    print("*"*15)
    for key, value in name_show_index.items():
        print("*", key, value)
    print("*"*15)

