# def show(age):
#     print("My age", age)

# huy_age = 17

# quang_anh_age = 29

# show(huy_age)

# show(quang_anh_age)

player = {
    "NAME": "Quang Anh",
    "HP": 60,
    "STR": 20,
    "DEF": 5,
    "LUCK": 10,
    "CRT": 6,
    "EXP": 1,
    "LVL": 1,
}

MiniZombie = {
    "NAME": "MiniZombie",
    "HP": 40,
    "STR": 17,
    "DEF": 7,
    "LUCK": 2,
    "EXP": 1,
    "LVL": 1,
}

# steal_gauntlet = {
#     "NAME": "Steal gauntlet",
#     "DEF": 5,
#     "STR": 5,
#     "AGI": 3,
# }
#
# bronze_shield = {
#     "NAME": "Bronze shield",
#     "DEF": 12,
#     "STR": 4,
#     "AGI": -5,
# }
#
# golden_stick = {
#     "NAME": "Golden stick",
#     "AGI": 15,
#     "HP": 20,
#     "STR": 100
# }

inventory = [player, MiniZombie]

def combat(attacker, defender):
    print(attacker["NAME"], "is beating", defender["NAME"])
    damage = attacker["STR"] - defender["DEF"]
    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "lost", damage, "HP")
    else:
        attacker["HP"] -= abs(damage)
        print(attacker["NAME"], "lost", abs(damage), "HP")

def show_index(name):
    print("*"*15)
    for key, value in name.items():
        print("*", key, value)
    print("*"*15)

while True:
    combat(player, MiniZombie)
    show_index(player)
    show_index(MiniZombie)
    if MiniZombie["HP"] <= 0:
        print("You win")
        break
    elif player["HP"] <= 0:
        print("Game over")
        break

    combat(MiniZombie, player)
    show_index(player)
    show_index(MiniZombie)
    if MiniZombie["HP"] <= 0:
        print("You win")
        break
    elif player["HP"] <= 0:
        print("Game over")
        break


