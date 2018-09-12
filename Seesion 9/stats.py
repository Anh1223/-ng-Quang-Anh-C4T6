from random import *

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

Orc = {
    "NAME": "MiniOrc",
    "CLASS": "Orc",
    "HP": 60,
    "STR": 5,
    "DEF": 2,
    "LUCK": 2,
    "AGI": 1,
    "LVL": 1,
}
player = {
    "NAME": "Anh1223",
    "CLASS": "Hacker",
    "HP": 60,
    "STR": 7,
    "DEF": 3,
    "LUCK": 5,
    "AGI": 2,
    "LVL": 1,
}

space_stone = {
    "NAME": "Space Stone",
    "HP": 0,
    "STR": 0,
    "DEF": 0,
    "LUCK": 70,
    "AGI": 200,
}
mind_stone = {
"NAME": "Mid Stone",
    "HP": 450,
    "STR": 30,
    "DEF": 60,
    "LUCK": 40,
    "AGI": 100,
}
reality_stone = {
    "NAME": "Reality Stone",
    "HP": 200,
    "STR": 350,
    "DEF": 100,
    "LUCK": -20,
    "AGI": -5,
}
power_stone = {
    "NAME": "Power Stone",
    "HP": 50,
    "STR": 10000,
    "DEF": 20,
    "LUCK": 10,
    "AGI": 7,
}
time_stone = {
    "NAME": "Time Stone",
    "HP": 100000,
    "STR": 0,
    "DEF": 0,
    "LUCK": 200,
    "AGI": 0,
}
soul_stone = {
    "NAME": "Soul Stone",
    "HP": -40,
    "STR": 10,
    "DEF": 400,
    "LUCK": 50,
    "AGI": 4,
}
gauntlet_infinity = {
    "NAME": "Gauntlet Infinity",
    "HP": 0,
    "STR": 50,
    "DEF": 10,
    "LUCK": 0,
    "AGI": -8,
}


def infinity(infinity_stone, số_infinity_stone, all_infinity_stone_on_gauntlet_infinity, all_index):
    for _ in range(số_infinity_stone):
        autopickstone = choice(infinity_stone)
        all_infinity_stone_on_gauntlet_infinity.append(autopickstone)
        infinity_stone.remove(autopickstone)

    for stone in all_infinity_stone_on_gauntlet_infinity:
        for i in all_index:
            gauntlet_infinity[i] += stone[i]

    if số_infinity_stone == 1:
        si = all_infinity_stone_on_gauntlet_infinity[0]
        gauntlet_infinity["NAME"] = "Gauntlet Infinity(", si["NAME"], ")"
    elif số_infinity_stone == 2:
        si0 = all_infinity_stone_on_gauntlet_infinity[0]
        si1 = all_infinity_stone_on_gauntlet_infinity[1]
        gauntlet_infinity["NAME"] = "Gauntlet Infinity(", si0["NAME"], si1["NAME"], ")"
    elif số_infinity_stone == 3:
        si0 = all_infinity_stone_on_gauntlet_infinity[0]
        si1 = all_infinity_stone_on_gauntlet_infinity[1]
        si2 = all_infinity_stone_on_gauntlet_infinity[2]
        gauntlet_infinity["NAME"] = "Gauntlet Infinity(", si0["NAME"], si1["NAME"], si2["NAME"], ")"
    elif số_infinity_stone == 4:
        si0 = all_infinity_stone_on_gauntlet_infinity[0]
        si1 = all_infinity_stone_on_gauntlet_infinity[1]
        si2 = all_infinity_stone_on_gauntlet_infinity[2]
        si3 = all_infinity_stone_on_gauntlet_infinity[3]
        gauntlet_infinity["NAME"] = "Gauntlet Infinity(", si0["NAME"], si1["NAME"], si2["NAME"], si3["NAME"], ")"
    elif số_infinity_stone == 5:
        si0 = all_infinity_stone_on_gauntlet_infinity[0]
        si1 = all_infinity_stone_on_gauntlet_infinity[1]
        si2 = all_infinity_stone_on_gauntlet_infinity[2]
        si3 = all_infinity_stone_on_gauntlet_infinity[3]
        si4 = all_infinity_stone_on_gauntlet_infinity[4]
        gauntlet_infinity["NAME"] = "Gauntlet Infinity(", si0["NAME"], si1["NAME"], si2["NAME"], si3["NAME"], si4["NAME"], ")"
    elif số_infinity_stone == 6:
        si0 = all_infinity_stone_on_gauntlet_infinity[0]
        si1 = all_infinity_stone_on_gauntlet_infinity[1]
        si2 = all_infinity_stone_on_gauntlet_infinity[2]
        si3 = all_infinity_stone_on_gauntlet_infinity[3]
        si4 = all_infinity_stone_on_gauntlet_infinity[4]
        si5 = all_infinity_stone_on_gauntlet_infinity[5]
        gauntlet_infinity["NAME"] = "Gauntlet Infinity(", si0["NAME"], si1["NAME"], si2["NAME"], si3["NAME"], si4["NAME"], si5["NAME"], ")"

