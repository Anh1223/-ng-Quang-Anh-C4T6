import random

NAME = input("Bạn tên gì?")

player = {              #ID: 0    (khi bị tấn công để random)
    "NAME": NAME,
    "HP": 400,
    "STR": 7,
    "DEF": 10,
    "LUCK": 10,
    "CRT": 6,
    "LVL": 1,
    "EXP": 0,
}

MiniZombie = {          #khi giết được 20 XP, 5 coin có tỉ lệ rơi đồ 1%   ID: 0
    "NAME": "MiniZombie",
    "HP": 40,
    "STR": 5,
    "DEF": 2,
    "LUCK": 2,
    "LVL": 1,
}

Zombie = {             #khi giết được 40 XP, 10 coin có tỉ lệ rơi đồ 2%   ID: 1
    "NAME": "Zombie",
    "HP": 80,
    "STR": 10,
    "DEF": 4,
    "LUCK": 4,
    "LVL": 1,
}

BigZombie = {          #khi giết được 80 XP, 10 coin có tỉ lệ rơi đồ 3%   ID:  2
    "NAME": "BigZombie",
    "HP": 160,
    "STR": 20,
    "DEF": 8,
    "LUCK": 8,
    "LVL": 1,
}

Bossphu = {           #khi giết được 100 XP, 50 coin có tỉ lệ rơi đồ 20%   ID: 3
    "NAME": "Boss phụ",
    "HP": 320,
    "STR": 20,
    "DEF": 8,
    "LUCK": 8,
    "LVL": 1,
}

MiniBoss = {             #khi giết được 200 XP, 30 coin có tỉ lệ rơi đồ 25%  ID: 4
    "NAME": "MiniBoss",
    "HP": 200,
    "STR": 12,
    "DEF": 12,
    "LUCK": 1,
    "LVL": 1,
}

TrumCuoi = {            #khi giết win game xác định là ở lever cuôi
    "NAME": "Trùm Cuối",
    "HP": 10000,
    "STR": 400,
    "DEF": 250,
    "LUCK": 50,
    "LVL": 500,
}

nameBot1_list = ["Bell", "Maximilan", "Ralph", "Juliet", "Gwen", "Axelle", "June", "Ambrose", "Bernice", "Daniel"]
nameBot1 = random.randint(0, 9)
Bot1 = {            #bot này xuất hiện trước  ID: 1   (khi bị tấn công để random)
    "NAME": nameBot1_list[nameBot1],
    "HP": 200,
    "STR": 14,
    "DEF": 8,
    "LUCK": 7,
    "CRT": 7,
    "LVL": 3,
    "EXP": 0,
}

nameBot2_list = ["Isaac", "Ash", "Centola", "Edgar", "Fay", "Dana", "Albert", "Darius", "Case", "Hubert"]
nameBot2 = random.randint(0, 9)
Bot2 = {           #ID: 2    (khi bị tấn công để random)
    "NAME": nameBot2_list[nameBot2],
    "HP": 476,
    "STR": 120,
    "DEF": 23,
    "LUCK": 34,
    "CRT": 34,
    "LVL": 45,
    "EXP": 0,
}

# def traloisai_cauhoidautien():

print("Xin chào", NAME,", tôi tên là:", Bot1["NAME"])
print("Bạn là một trong những người may mắn còn sống trong trận đại dịch Zombie")
print("Bạn phải sống sót và tập hợp những người sống sót,")
print("đi tìm nơi ở của Zombie mẹ")
print("Vậy bạn có đi tìm Zombie mẹ cùng tôi không")
print("1. Có")
print("2. Không")
dichuen = input("")
if dichuen == "1":
    print("Ở đằng kia có rất nhiều Zombie, có thể có Zombie mẹ ở đó")
    spawn = random.randint(0,2)
    if spawn == 0:
        solanlap = [0]
        for _ in solanlap:
            Luck = random.randint(MiniZombie["LUCK"], 100)
            if Luck < 80:
                damageBot1 = Bot1["STR"] - MiniZombie["DEF"]
                if damageBot1 > 0 :
                    MiniZombie["HP"] -= damageBot1
            Luck = random.randint(MiniZombie["LUCK"], 100)
            if Luck < 80:
                damageplayer = player["STR"] - MiniZombie["DEF"]
                if damageplayer > 0 :
                    MiniZombie["HP"] -= damageplayer
                damageMiniZombie = MiniZombie["STR"] - player["DEF"]
                if damageMiniZombie > 0:
                    Zombietancong = random.random()
                    if Zombietancong == 0:
                        Luck = random.randint(player["LUCK"], 100)
                        if Luck < 80:
                            player["HP"] -= damageMiniZombie
                    elif Zombietancong == 1:
                        Luck = random.randint(Bot1["LUCK"], 100)
                        if Luck < 80:
                            Bot1["HP"] -= damageMiniZombie
            if MiniZombie["HP"] < 0:
                MiniZombie["HP"] = 0
            if player["HP"] < 0:
                player["HP"] = 0
            if Bot1["HP"] < 0:
                Bot1["HP"] = 0
            print(player)
            print(Bot1)
            print(MiniZombie)
            if MiniZombie["HP"] == 0:
                print("Your kill 1 Zombie")
                if player["HP"] > 0:
                    player["EXP"] = player["EXP"] + 20
                if Bot1["HP"] > 0:
                    Bot1["EXP"] = Bot1["EXP"] + 20
                print("Your EXP:", player["EXP"])
            elif player["HP"] == 0:
                print("Your die")
                print("GAME OVER")
            elif Bot1["HP"] == 0:
                print("Bạn hãy cố gắng giải cứu thế giới")
                print("VĨNH BIỆT!!!")
                print(Bot1["NAME"],": DIE")
            else:
                solanlap.append(_)
    elif spawn == 1:
        solanlap = [0]
        for _ in solanlap:
            Luck = random.randint(Zombie["LUCK"], 100)
            if Luck < 80:
                damageBot1 = Bot1["STR"] - Zombie["DEF"]
                if damageBot1 > 0:
                    Zombie["HP"] -= damageBot1
            Luck = random.randint(Zombie["LUCK"], 100)
            if Luck < 80:
                damageplayer = player["STR"] - Zombie["DEF"]
                if damageplayer > 0:
                    Zombie["HP"] -= damageplayer
                damageZombie = Zombie["STR"] - player["DEF"]
                if damageZombie > 0:

                    Zombietancong = random.random()
                    if Zombietancong == 0:
                        Luck = random.randint(player["LUCK"], 100)
                        if Luck < 80:
                            player["HP"] -= damageZombie
                    elif Zombietancong == 1:
                        Luck = random.randint(Bot1["LUCK"], 100)
                        if Luck < 80:
                            Bot1["HP"] -= damageZombie
            if Zombie["HP"] < 0:
                Zombie["HP"] = 0
            if player["HP"] < 0:
                player["HP"] = 0
            if Bot1["HP"] < 0:
                Bot1["HP"] = 0
            print(player)
            print(Bot1)
            print(Zombie)
            if Zombie["HP"] == 0:
                print("Your kill 1 Zombie")
                if player["HP"] > 0:
                    player["EXP"] = player["EXP"] + 20
                if Bot1["HP"] > 0:
                    Bot1["EXP"] = Bot1["EXP"] + 20
                print("Your EXP:", player["EXP"])
            elif player["HP"] == 0:
                print("Your die")
                print("GAME OVER")
            elif Bot1["HP"] == 0:
                print("Bạn hãy cố gắng giải cứu thế giới")
                print("VĨNH BIỆT!!!")
                print(Bot1["NAME"], ": DIE")
            else:
                solanlap.append(_)
    elif spawn == 2:
        solanlap = [0]
        for _ in solanlap:
            Luck = random.randint(BigZombie["LUCK"], 100)
            if Luck < 80:
                damageBot1 = Bot1["STR"] - BigZombie["DEF"]
                if damageBot1 > 0:
                    BigZombie["HP"] -= damageBot1
            Luck = random.randint(BigZombie["LUCK"], 100)
            if Luck < 80:
                damageplayer = player["STR"] - BigZombie["DEF"]
                if damageplayer > 0:
                    BigZombie["HP"] -= damageplayer
                damageBigZombie = BigZombie["STR"] - player["DEF"]
                if damageBigZombie > 0:
                    Zombietancong = random.random()
                    if Zombietancong == 0:
                        Luck = random.randint(player["LUCK"], 100)
                        if Luck < 80:
                            player["HP"] -= damageBigZombie
                    elif Zombietancong == 1:
                        Luck = random.randint(Bot1["LUCK"], 100)
                        if Luck < 80:
                            Bot1["HP"] -= damageBigZombie
            if BigZombie["HP"] < 0:
                BigZombie["HP"] = 0
            if player["HP"] < 0:
                player["HP"] = 0
            if Bot1["HP"] < 0:
                Bot1["HP"] = 0
            print(player)
            print(Bot1)
            print(BigZombie)
            if BigZombie["HP"] == 0:
                print("Your kill 1 Zombie")
                if player["HP"] > 0:
                    player["EXP"] = player["EXP"] + 20
                if Bot1["HP"] > 0:
                    Bot1["EXP"] = Bot1["EXP"] + 20
                print("Your EXP:", player["EXP"])
            elif player["HP"] == 0:
                print("Your die")
                print("GAME OVER")
            elif Bot1["HP"] == 0:
                print("Bạn hãy cố gắng giải cứu thế giới")
                print("VĨNH BIỆT!!!")
                print(Bot1["NAME"], ": DIE")
            else:
                solanlap.append(_)
elif dichuen == "2":
    print("Bạn ở lại một mình và chết đói vì không có thức ăn")
    print("GAME OVER")
else :
    print("Tôi không hiểu ý bạn, bạn hãy trả lời lại")
