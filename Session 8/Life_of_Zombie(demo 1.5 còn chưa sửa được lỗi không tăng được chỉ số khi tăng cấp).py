from random import *

NAME = input("Bạn tên gì?")

player = {  # ID: 0    (khi bị tấn công để random)
    "NAME": NAME,
    "HP": 400,
    "STR": 10,
    "DEF": 10,
    "LUCK": 10,
    "CRT": 6,
    "EXP": 1,
    "LVL": 1,
}

player_macdinh = {  # ID: 0    (khi bị tấn công để random)
    "NAME": NAME,
    "HP": 400,
    "STR": 10,
    "DEF": 10,
    "LUCK": 10,
    "CRT": 6,
    "EXP": 1,
    "LVL": 1,
}

MiniZombie = {  # khi giết được 20 XP, 5 coin có tỉ lệ rơi đồ 1%   ID: 0
    "NAME": "MiniZombie",
    "HP": 40,
    "STR": 6,
    "DEF": 2,
    "LUCK": 2,
    "CRT": 2,
    "EXP": 1,
    "LVL": 1,  # MiniZombie["EXP"]/100,
}

Zombie = {  # khi giết được 40 XP, 10 coin có luck rơi đồ 2   ID: 1
    "NAME": "Zombie",
    "HP": 80,
    "STR": 10,
    "DEF": 4,
    "LUCK": 4,
    "CRT": 4,
    "EXP": 1,
    "LVL": 1,  # Zombie["EXP"]/100,
}

BigZombie = {  # khi giết được 80 XP, 10 coin có luck rơi đồ 3   ID:  2
    "NAME": "BigZombie",
    "HP": 160,
    "STR": 20,
    "DEF": 8,
    "LUCK": 8,
    "CRT": 8,
    "EXP": 1,
    "LVL": 1,  # BigZombie["EXP"]/100,
}

Bossphu = {  # khi giết được 100 XP, 50 coin có luck rơi đồ 20   ID: 3
    "NAME": "Boss phụ",
    "HP": 320,
    "STR": 20,
    "DEF": 8,
    "LUCK": 8,
    "CRT": 10,
    "EXP": 1,
    "LVL": 20,  # Bossphu["EXP"]/100,
}

MiniBoss = {  # khi giết được 200 XP, 30 coin có luck rơi đồ 25  ID: 4
    "NAME": "MiniBoss",
    "HP": 200,
    "STR": 12,
    "DEF": 12,
    "LUCK": 1,
    "CRT": 10,
    "EXP": 1,
    "LVL": 45,  # MiniBoss["EXP"]/100,
}

TrumCuoi = {  # khi giết win game xác định là cho nó ở lever cuôi
    "NAME": "Giê-su",
    "HP": 2300000,
    "STR": 400,
    "DEF": 250,
    "LUCK": 70,
    "CRT": 30,
    "LVL": "Chưa xác định được",
}

MiniZombie_macdinh = {  # khi giết được 20 XP, 5 coin có tỉ lệ rơi đồ 1%   ID: 0
    "NAME": "MiniZombie",
    "HP": 40,
    "STR": 6,
    "DEF": 2,
    "LUCK": 2,
    "CRT": 2,
    "EXP": 1,
    "LVL": 1,  # MiniZombie["EXP"]/100,
}

Zombie_macdinh = {  # khi giết được 40 XP, 10 coin có luck rơi đồ 2   ID: 1
    "NAME": "Zombie",
    "HP": 80,
    "STR": 10,
    "DEF": 4,
    "LUCK": 4,
    "CRT": 4,
    "EXP": 1,
    "LVL": 1,  # Zombie["EXP"]/100,
}

BigZombie_macdinh = {  # khi giết được 80 XP, 10 coin có luck rơi đồ 3   ID:  2
    "NAME": "BigZombie",
    "HP": 160,
    "STR": 20,
    "DEF": 8,
    "LUCK": 8,
    "CRT": 8,
    "EXP": 1,
    "LVL": 1,  # BigZombie["EXP"]/100,
}

Bossphu_macdinh = {  # khi giết được 100 XP, 50 coin có luck rơi đồ 20   ID: 3
    "NAME": "Boss phụ",
    "HP": 320,
    "STR": 20,
    "DEF": 8,
    "LUCK": 8,
    "CRT": 10,
    "EXP": 1,
    "LVL": 20,  # Bossphu["EXP"]/100,
}

MiniBoss_macdinh = {  # khi giết được 200 XP, 30 coin có luck rơi đồ 25  ID: 4
    "NAME": "MiniBoss",
    "HP": 200,
    "STR": 12,
    "DEF": 12,
    "LUCK": 1,
    "CRT": 10,
    "EXP": 1,
    "LVL": 45,  # MiniBoss["EXP"]/100,
}

TrumCuoi_macdinh = {  # khi giết win game xác định là cho nó ở lever cuôi
    "NAME": "Giê-su",
    "HP": 2300000,
    "STR": 400,
    "DEF": 250,
    "LUCK": 70,
    "CRT": 30,
    "LVL": "Chưa xác định được",
}

nameBot1_list = ["Bell", "Maximilan", "Ralph", "Juliet", "Gwen", "Axelle", "June", "Ambrose", "Bernice", "Daniel"]
nameBot1 = randint(0, 9)
Bot1 = {  # bot này xuất hiện trước  ID: 1   (khi bị tấn công để random)
    "NAME": nameBot1_list[nameBot1],
    "HP": 200,
    "STR": 14,
    "DEF": 8,
    "LUCK": 7,
    "CRT": 7,
    "EXP": 1,
    "LVL": 1,  # Bot1["EXP"]/100,
}

Bot1_macdinh = {  # bot này xuất hiện trước  ID: 1   (khi bị tấn công để random)
    "NAME": nameBot1_list[nameBot1],
    "HP": 200,
    "STR": 14,
    "DEF": 8,
    "LUCK": 7,
    "CRT": 7,
    "EXP": 1,
    "LVL": 1,  # Bot1["EXP"]/100,
}

nameBot2_list = ["Isaac", "Ash", "Centola", "Edgar", "Fay", "Dana", "Albert", "Darius", "Case", "Hubert"]
nameBot2 = randint(0, 9)
Bot2 = {  # ID: 2    (khi bị tấn công để random)
    "NAME": nameBot2_list[nameBot2],
    "HP": 476,
    "STR": 120,
    "DEF": 23,
    "LUCK": 34,
    "CRT": 34,
    "EXP": 1,
    "LVL": 34,  # Bot2["EXP"]/100,
}


nhanvat = [player, Bot1, Bot2]
loai_Zombie = [MiniZombie, Zombie, BigZombie, Bossphu, MiniBoss, TrumCuoi]
tonghop = []
cacloaivukhi_MiniZombie = []
cacloaivukhi_Zombie = []
cacloaivukhi_BigZombie = []


def show_index(name):
    print("*" * 15)
    for key, value in name.items():
        print("*", key, value)
    print("*" * 15)


def tinh_combat(nameplayer, nameBot1, nameZombie, traloicauhoi_dokho_tq, spawn_tq):
    print("Thông số zombie chuẩn bị tấn công:")
    show_index(nameZombie)
    while True:

        print("Tấn công or Phòng thủ")
        print("1. Tấn công")
        print("2. Phòng thủ")


        DEFtamthoiZombie = nameZombie["DEF"] * randint(0, 2)
        DEFtamthoiplayer = nameplayer["DEF"] * randint(0, 2)
        DEFtamthoiBot = nameBot1["DEF"] * randint(0, 2)

        damageplayerlenZombiecong = nameplayer["STR"] * randint(1, 2) - nameZombie["DEF"]
        damageplayerlenZombiethu = nameplayer["STR"] * randint(1, 2) - DEFtamthoiZombie

        damageBot1lenZombiecong = nameBot1["STR"] * randint(1, 2) - nameZombie["DEF"]
        damageBot1lenZombiethu = nameBot1["STR"] * randint(1, 2) - DEFtamthoiZombie

        damageZombielenplayercong = nameZombie["STR"] * randint(1, 2) - nameplayer["DEF"]
        damageZombielenplayerthu = nameZombie["STR"] * randint(1, 2) - DEFtamthoiplayer

        damageZombielenBot1cong = nameZombie["STR"] * randint(1, 2) - nameBot1["DEF"]
        damageZombielenBot1thu = nameZombie["STR"] * randint(1, 2) - DEFtamthoiBot

        LuckZombie = randint(nameZombie["LUCK"], 100)
        Luckplayer = randint(nameplayer["LUCK"], 100)
        LuckBot1 = randint(nameBot1["LUCK"], 100)

        tancong_phongthu_player = int(input(" "))
        tancong_phongthu_Bot1 = randint(0, 1)
        tancong_phongthu_Zombie = randint(0, 1)

        if damageZombielenplayercong < 0:
            damageZombielenplayercong = 0
        if damageZombielenplayerthu < 0:
            damageZombielenplayerthu = 0
        if damageZombielenBot1cong < 0:
            damageZombielenBot1cong = 0
        if damageZombielenBot1thu < 0:
            damageZombielenBot1thu = 0

        if traloicauhoi_dokho_tq == "1":
            if damageBot1lenZombiethu < 0:
                damageBot1lenZombiethu = 0
            if damageBot1lenZombiecong < 0:
                damageBot1lenZombiecong = 0
            if damageplayerlenZombiecong < 0:
                damageplayerlenZombiecong = 0
            if damageplayerlenZombiethu < 0:
                damageplayerlenZombiethu = 0

        if tancong_phongthu_player == 1:
            if LuckZombie < 80:
                if tancong_phongthu_Zombie == 0:
                    nameZombie["HP"] -= damageplayerlenZombiecong
                if tancong_phongthu_Zombie == 1:
                    nameZombie["HP"] -= damageplayerlenZombiethu

        if nameBot1["HP"] > 0:
            if tancong_phongthu_Bot1 == 0:
                if LuckZombie < 80:
                    if tancong_phongthu_Zombie == 0:
                        nameZombie["HP"] -= damageBot1lenZombiecong
                    if tancong_phongthu_Zombie == 1:
                        nameZombie["HP"] -= damageBot1lenZombiethu

        if tancong_phongthu_Zombie == 0:
            if Luckplayer < 80:
                if tancong_phongthu_player == 1:
                    nameplayer["HP"] -= damageZombielenplayercong
                if tancong_phongthu_player == 2:
                    nameplayer["HP"] -= damageZombielenplayerthu

            if LuckBot1 < 80:
                if tancong_phongthu_Bot1 == 0:
                    nameBot1["HP"] -= damageZombielenBot1cong
                if tancong_phongthu_player == 1:
                    nameBot1["HP"] -= damageZombielenBot1thu

        if nameZombie["HP"] < 0:
            nameZombie["HP"] = 0
        if nameplayer["HP"] < 0:
            nameplayer["HP"] = 0
        if nameBot1["HP"] < 0:
            nameBot1["HP"] = 0
        show_index(nameplayer)
        Bot1chetgoc = [0]
        Bot1chetsosanh = [0]
        if nameBot1["HP"] >= 0:
            if Bot1chetgoc == Bot1chetsosanh:
                show_index(nameBot1)
        show_index(nameZombie)
        if nameZombie["HP"] == 0:
            print("Your kill 1 Zombie")
            if spawn_tq == 0:
                nameZombie["HP"] = 40
            elif spawn_tq == 1:
                nameZombie["HP"] = 80
            elif spawn_tq == 2:
                nameZombie["HP"] = 160
            elif spawn_tq == 3:
                nameZombie["HP"] = 320
            elif spawn_tq == 4:
                nameZombie["HP"] = 200
            if spawn_tq == 0:
                nameZombie["EXP"] = 20
            elif spawn_tq == 1:
                nameZombie["EXP"] = 40
            elif spawn_tq == 2:
                nameZombie["EXP"] = 80
            elif spawn_tq == 3:
                nameZombie["EXP"] = 100
            elif spawn_tq == 4:
                nameZombie["EXP"] = 200
            while True:
                if nameZombie["EXP"] > 100:
                    nameZombie["EXP"] -= 100
                    nameZombie["LVL"] += 1
                    if nameZombie["LUCK"] < 70:
                        loaicantang = randint(2, 5)
                        if loaicantang == 2:
                            nameZombie["STR"] += 10
                        elif loaicantang == 3:
                            nameZombie["DEF"] += 10
                        elif loaicantang == 4:
                            nameZombie["LUCK"] += 10
                        elif loaicantang == 5:
                            nameZombie["CRT"] += 10

                    elif nameZombie["LUCK"] >= 70:
                        loaicantang = randint(2, 4)
                        if loaicantang == 2:
                            nameZombie["STR"] += 10
                        elif loaicantang == 3:
                            nameZombie["DEF"] += 10
                        elif loaicantang == 4:
                            nameZombie["LUCK"] += 10
                if nameZombie["EXP"] < 100:
                    break

            if nameplayer["HP"] > 0:
                nameplayer["EXP"] += 20
                while True:
                    if nameplayer["EXP"] > 100:
                        nameplayer["LVL"] += 1
                        print("Bạn đã lên LVL:", nameplayer["LVL"])
                        nameplayer["EXP"] -= 100
                        if nameplayer["LUCK"] < 70:
                            while True:
                                print("Bạn muốn tăng")
                                print("*" * 100)
                                print("1. HP")
                                print("2. STR")
                                print("3. DEF")
                                print("4.LUCK")
                                print("5. CRT")
                                print("Lưu ý: bạn chọn mục nào thì chỉ số mục đấy tăng 10")
                                print("*" * 100)
                                loaicantang = input(" ")
                                loaicantang = loaicantang.lower()
                                if loaicantang == "1" or "hp":
                                    nameplayer["HP"] += 10
                                    break
                                elif loaicantang == "2" or "str":
                                    nameplayer["STR"] += 10
                                    break
                                elif loaicantang == "3" or "def":
                                    nameplayer["DEF"] += 10
                                    break
                                elif loaicantang == "4" or "luck":
                                    nameplayer["LUCK"] += 10
                                    break
                                elif loaicantang == "5" or "crt":
                                    nameplayer["CRT"] += 10
                                    break
                                else:
                                    print("Bạn không có thông số:", loaicantang)
                                    print("Bạn hãy nhập lại")

                        elif nameplayer["LUCK"] >= 70:
                            while True:
                                print("Vì LUCK của bạn đã MAX nên không xuất hiện trong bảng")
                                print("Bạn muốn tăng,lưu ý: CRT hiện giờ vô dụng, bạn không nên tăng")
                                print("*" * 100)
                                print("1. HP")
                                print("2. STR")
                                print("3. DEF")
                                print("4.LUCK")
                                print("5. CRT")
                                print("Lưu ý: bạn chọn mục nào thì chỉ số mục đấy tăng 10")
                                print("*" * 100)
                                loaicantang = input(" ")
                                loaicantang = loaicantang.lower()
                                if loaicantang == "1" or "hp":
                                    nameplayer["HP"] += 10
                                    break
                                elif loaicantang == "2" or "str":
                                    nameplayer["STR"] += 10
                                    break
                                elif loaicantang == "3" or "def":
                                    nameplayer["DEF"] += 10
                                    break
                                elif loaicantang == "4" or "luck":
                                    nameplayer["LUCK"] += 10
                                    break
                                elif loaicantang == "5" or "crt":
                                    nameplayer["CRT"] += 10
                                    break
                                else:
                                    print("Bạn không có thông số:", loaicantang)
                                    print("Bạn hãy nhập lại")
                    if nameplayer["EXP"] < 100:
                        break


            if nameBot1["HP"] > 0:
                nameBot1["EXP"] += 20
                while True:
                    if nameBot1["EXP"] > 100:
                        nameBot1["LVL"] += 1
                        nameBot1["EXP"] -= 100
                        if nameBot1["LUCK"] < 70:
                            loaicantang = randint(2, 5)
                            if loaicantang == 2:
                                nameBot1["STR"] += 10
                            elif loaicantang == 3:
                                nameBot1["DEF"] += 10
                            elif loaicantang == 4:
                                nameBot1["LUCK"] += 10
                            elif loaicantang == 5:
                                nameBot1["CRT"] += 10

                        elif nameBot1["LUCK"] >= 70:
                            loaicantang = randint(2, 4)
                            if loaicantang == 2:
                                nameBot1["STR"] += 10
                            elif loaicantang == 3:
                                nameBot1["DEF"] += 10
                            elif loaicantang == 4:
                                nameBot1["CRT"] += 10
                    if nameBot1["EXP"] < 100:
                        break
            break

        if nameplayer["HP"] == 0:
            print("Your die")
            while True:
                print("Nếu muốn chơi lại hãy nhập (replay)")
                choilai = input(" ")
                choilai = choilai.lower()
                if choilai == "replay":
                    nameplayer = player_macdinh
                    nameBot1 = Bot1_macdinh
                    MiniZombie = MiniZombie_macdinh
                    Zombie = Zombie_macdinh
                    BigZombie = BigZombie_macdinh
                    print(nameplayer)
                    cottruyen(nameplayer, nameBot1, nameZombie)
                    break
                else:
                    print("Xin nhập lại")


def tinh_combat_khongcoBot(nameplayer, nameZombie, traloicauhoi_dokho_tq, spawn_tq):
    print("Thông số zombie chuẩn bị tấn công:")
    show_index(nameZombie)
    while True:

        print("Tấn công or Phòng thủ")
        print("1. Tấn công")
        print("2. Phòng thủ")

        DEFtamthoiZombie = nameZombie["DEF"] * randint(0, 2)
        DEFtamthoiplayer = nameplayer["DEF"] * randint(0, 2)

        damageplayerlenZombiecong = nameplayer["STR"] * randint(1, 2) - nameZombie["DEF"]
        damageplayerlenZombiethu = nameplayer["STR"] * randint(1, 2) - DEFtamthoiZombie

        damageZombielenplayercong = nameZombie["STR"] * randint(1, 2) - nameplayer["DEF"]
        damageZombielenplayerthu = nameZombie["STR"] * randint(1, 2) - DEFtamthoiplayer

        LuckZombie = randint(nameZombie["LUCK"], 100)
        Luckplayer = randint(nameplayer["LUCK"], 100)

        tancong_phongthu_player = int(input(" "))
        tancong_phongthu_Zombie = randint(0, 1)

        if damageZombielenplayercong < 0:
            damageZombielenplayercong = 0
        if damageZombielenplayerthu < 0:
            damageZombielenplayerthu = 0

        if traloicauhoi_dokho_tq == "1":
            if damageplayerlenZombiecong < 0:
                damageplayerlenZombiecong = 0
            if damageplayerlenZombiethu < 0:
                damageplayerlenZombiethu = 0

        if tancong_phongthu_player == 1:
            if LuckZombie < 80:
                if tancong_phongthu_Zombie == 0:
                    nameZombie["HP"] -= damageplayerlenZombiecong
                if tancong_phongthu_Zombie == 1:
                    nameZombie["HP"] -= damageplayerlenZombiethu

        if tancong_phongthu_Zombie == 0:
            if Luckplayer < 80:
                if tancong_phongthu_player == 1:
                    nameplayer["HP"] -= damageZombielenplayercong
                if tancong_phongthu_player == 2:
                    nameplayer["HP"] -= damageZombielenplayerthu

        if nameZombie["HP"] < 0:
            nameZombie["HP"] = 0
        if nameplayer["HP"] < 0:
            nameplayer["HP"] = 0
        show_index(nameplayer)
        show_index(nameZombie)
        if nameZombie["HP"] == 0:
            print("Your kill 1 Zombie")
            if spawn_tq == 0:
                nameZombie["HP"] = 40
            elif spawn_tq == 1:
                nameZombie["HP"] = 80
            elif spawn_tq == 2:
                nameZombie["HP"] = 160
            elif spawn_tq == 3:
                nameZombie["HP"] = 320
            elif spawn_tq == 4:
                nameZombie["HP"] = 200
            if spawn_tq == 0:
                nameZombie["EXP"] = 20
            elif spawn_tq == 1:
                nameZombie["EXP"] = 40
            elif spawn_tq == 2:
                nameZombie["EXP"] = 80
            elif spawn_tq == 3:
                nameZombie["EXP"] = 100
            elif spawn_tq == 4:
                nameZombie["EXP"] = 200
            while True:
                if nameZombie["EXP"] > 100:
                    nameZombie["EXP"] -= 100
                    nameZombie["LVL"] += 1
                    if nameZombie["LUCK"] < 70:
                        loaicantang = randint(2, 5)
                        if loaicantang == 2:
                            nameZombie["STR"] += 10
                        elif loaicantang == 3:
                            nameZombie["DEF"] += 10
                        elif loaicantang == 4:
                            nameZombie["LUCK"] += 10
                        elif loaicantang == 5:
                            nameZombie["CRT"] += 10

                    elif nameZombie["LUCK"] >= 70:
                        loaicantang = randint(2, 4)
                        if loaicantang == 2:
                            nameZombie["STR"] += 10
                        elif loaicantang == 3:
                            nameZombie["DEF"] += 10
                        elif loaicantang == 4:
                            nameZombie["LUCK"] += 10
                if nameZombie["EXP"] < 100:
                    break

            if nameplayer["HP"] > 0:
                nameplayer["EXP"] += 20
                while True:
                    if nameplayer["EXP"] > 100:
                        nameplayer["LVL"] += 1
                        print("Bạn đã lên LVL:", nameplayer["LVL"])
                        nameplayer["EXP"] -= 100
                        if nameplayer["LUCK"] < 70:
                            while True:
                                print("Bạn muốn tăng")
                                print("*" * 100)
                                print("1. HP")
                                print("2. STR")
                                print("3. DEF")
                                print("4.LUCK")
                                print("5. CRT")
                                print("Lưu ý: bạn chọn mục nào thì chỉ số mục đấy tăng 10")
                                print("*" * 100)
                                loaicantang = input(" ")
                                loaicantang = loaicantang.lower()
                                if loaicantang == "1" or "hp":
                                    nameplayer["HP"] += 10
                                    break
                                elif loaicantang == "2" or "str":
                                    nameplayer["STR"] += 10
                                    break
                                elif loaicantang == "3" or "def":
                                    nameplayer["DEF"] += 10
                                    break
                                elif loaicantang == "4" or "luck":
                                    nameplayer["LUCK"] += 10
                                    break
                                elif loaicantang == "5" or "crt":
                                    nameplayer["CRT"] += 10
                                    break
                                else:
                                    print("Bạn không có thông số:", loaicantang)
                                    print("Bạn hãy nhập lại")

                        elif nameplayer["LUCK"] >= 70:
                            while True:
                                print("Vì LUCK của bạn đã MAX nên không xuất hiện trong bảng")
                                print("Bạn muốn tăng,lưu ý: CRT hiện giờ vô dụng, bạn không nên tăng")
                                print("*" * 100)
                                print("1. HP")
                                print("2. STR")
                                print("3. DEF")
                                print("4.LUCK")
                                print("5. CRT")
                                print("Lưu ý: bạn chọn mục nào thì chỉ số mục đấy tăng 10")
                                print("*" * 100)
                                loaicantang = input(" ")
                                loaicantang = loaicantang.lower()
                                if loaicantang == "1" or "hp":
                                    nameplayer["HP"] += 10
                                    break
                                elif loaicantang == "2" or "str":
                                    nameplayer["STR"] += 10
                                    break
                                elif loaicantang == "3" or "def":
                                    nameplayer["DEF"] += 10
                                    break
                                elif loaicantang == "4" or "luck":
                                    nameplayer["LUCK"] += 10
                                    break
                                elif loaicantang == "5" or "crt":
                                    nameplayer["CRT"] += 10
                                    break
                                else:
                                    print("Bạn không có thông số:", loaicantang)
                                    print("Bạn hãy nhập lại")
                    if nameplayer["EXP"] < 100:
                        break
            break

        if nameplayer["HP"] == 0:
            print("Your die")
            while True:
                print("Nếu muốn chơi lại hãy nhập (replay)")
                choilai = input(" ")
                choilai = choilai.lower()
                if choilai == "replay":
                    nameplayer = player_macdinh
                    nameBot1 = Bot1_macdinh
                    MiniZombie = MiniZombie_macdinh
                    Zombie = Zombie_macdinh
                    BigZombie = BigZombie_macdinh
                    Bossphu = Bossphu_macdinh
                    MiniBoss = MiniZombie_macdinh
                    cottruyen(nameplayer, nameBot1, nameZombie)
                    break
                else:
                    print("Xin nhập lại")


def cottruyen(nameplayer, nameBot1, loai_Zombie_tq):
    print("Game này cho bạn vào một thế giới hỗn độn với Zombie ở khắp nơi bạn phải giết được Giê-su(thằng này nó già quá,")
    print(" bị bệnh thần kinh và đã tạo ra Zombie để hủy diệt loài người là) để chiến thắng(game này có thể có lỗi và chưa")
    print(" được tối ưu, hoàn thiện mọi command xin liên hệ Administrators: link FaceBook https://www.facebook.com/profile.php?id=100014034901974)")

    while True:
        print("Bạn hãy chọn độ khó")
        print("1. Dễ")
        print("2. khó(khi DEF của kẻ địch hơn STR của nhân vật thì kẻ địch được tăng máu)")
        traloicauhoi_dokho = input(" ")
        if traloicauhoi_dokho == "1":
            print("Chế độ: Dễ")
            break
        elif traloicauhoi_dokho == "2":
            print("Chế độ: Khó")
            break
        else:
            print("Chỉ được nhập 1(Chế độ: Dễ) hoặc 2(Chế độ: Khó)")

    while True:

        print("Để bắt đầu chơi hãy nhập (play)")
        print("hoặc bạn có thể xem thông số của bạn bằng cách nhập (stats)")
        gioithieugame = input(" ")
        gioithieugame = gioithieugame.lower()

        if gioithieugame == "cmd_hack":
            cmd_hack = input(" ")
            if cmd_hack == "hack_stats":
                hack_stats = input(" ")
                if hack_stats == "add_stats":
                    print("Tất cả chỉ số sẽ được tăng 1000 và LUCK sẽ được tăng max là 70")
                    nameplayer["HP"] += 1000
                    nameplayer["STR"] += 1000
                    nameplayer["DEF"] += 1000
                    nameplayer["LUCK"] = 70
                    nameplayer["CRT"] += 1000

        if gioithieugame == "stats":
            show_index(player)

        elif gioithieugame == "play":
            print("Xin chào", NAME, ", tôi tên là:", Bot1["NAME"])
            print("Bạn là một trong những người may mắn còn sống trong trận đại dịch Zombie")
            print("Bạn phải sống sót và tập hợp những người sống sót,")
            print("đi tìm nơi ở của Giê-su Zombie, giết nó và bạn sẽ giải cứu được thế giới")
            print("Vậy bạn có đi tìm Giê-su Zombie cùng tôi không")
            print("1. Có")
            print("2. Không")

            dichuen = input("")

            if dichuen == "1":
                print("Ở đằng kia có rất nhiều Zombie, có thể có Giê-su Zombie ở đó")
                print("1. Đi ra đó")
                print("2. Ở lại")
                dichuen = input(" ")
                if dichuen == "1":
                    soluongzombie = range(randint(10, 20))
                    print("Ở đó có:", max(soluongzombie) + 1, "con Zombie")
                    for slzb in soluongzombie:
                        spawn = randint(0, 2)
                        tinh_combat(nameplayer, nameBot1, loai_Zombie_tq[spawn], traloicauhoi_dokho, spawn)
                elif dichuen == "2":
                    print("Vì bạn đã đi ra khỏi nơi an toàn nên có rất nhiều Zombie xung quanh bạn bạn")
                    soluongzombie = range(randint(10, 20))
                    print("Quanh bạn có:", max(soluongzombie) + 1, "con Zombie")
                    for slzb in soluongzombie:
                        spawn = randint(0, 2)
                        tinh_combat_khongcoBot(nameplayer, loai_Zombie_tq[spawn], traloicauhoi_dokho, spawn)
                    print("Vì bạn giết quá nhiều Zombie nên Giê-Su đã sai 2 con quái vật mạnh hơn xuống để trừ khử", nameplayer["NAME"])





            elif dichuen == "2":
                while True:
                    print("Bạn ở lại một mình và chết đói vì không có thức ăn")
                    print("GAME OVER")
                    while True:
                        print("Nếu muốn chơi lại hãy nhập (replay)")
                        choilai = input(" ")
                        choilai = choilai.lower()
                        if choilai == "replay":
                            nameplayer = player_macdinh
                            cottruyen(nameplayer, nameBot1, loai_Zombie_tq)
                            break
                        else:
                            print("Xin nhập lại")

            else:

                print("Tôi không hiểu ý bạn, bạn hãy trả lời lại")



        else:
            if gioithieugame != "cmd_hack":
                print("Command của bạn không có trong từ điển của chúng tôi")
                print("Xin bạn hãy nhập lại")


cottruyen(player, Bot1, loai_Zombie)

