import random

NAME = input("Bạn tên gì?")

player = {              #ID: 0    (khi bị tấn công để random)
    "NAME": NAME,
    "HP": 400,
    "STR": 10,
    "DEF": 10,
    "LUCK": 10,
    "CRT": 6,
    "EXP": 1,
    "LVL": 1,
}

MiniZombie = {          #khi giết được 20 XP, 5 coin có tỉ lệ rơi đồ 1%   ID: 0
    "NAME": "MiniZombie",
    "HP": 40,
    "STR": 5,
    "DEF": 2,
    "LUCK": 2,
    "EXP": 1,
    "LVL": 1,#MiniZombie["EXP"]/100,
}

Zombie = {             #khi giết được 40 XP, 10 coin có luck rơi đồ 2   ID: 1
    "NAME": "Zombie",
    "HP": 80,
    "STR": 10,
    "DEF": 4,
    "LUCK": 4,
    "EXP": 1,
    "LVL": 1,#Zombie["EXP"]/100,
}

BigZombie = {          #khi giết được 80 XP, 10 coin có luck rơi đồ 3   ID:  2
    "NAME": "BigZombie",
    "HP": 160,
    "STR": 20,
    "DEF": 8,
    "LUCK": 8,
    "EXP": 1,
    "LVL": 1,#BigZombie["EXP"]/100,
}

Bossphu = {           #khi giết được 100 XP, 50 coin có luck rơi đồ 20   ID: 3
    "NAME": "Boss phụ",
    "HP": 320,
    "STR": 20,
    "DEF": 8,
    "LUCK": 8,
    "EXP": 1,
    "LVL": 20,#Bossphu["EXP"]/100,
}

MiniBoss = {             #khi giết được 200 XP, 30 coin có luck rơi đồ 25  ID: 4
    "NAME": "MiniBoss",
    "HP": 200,
    "STR": 12,
    "DEF": 12,
    "LUCK": 1,
    "EXP": 1,
    "LVL": 45,#MiniBoss["EXP"]/100,
}

TrumCuoi = {            #khi giết win game xác định là cho nó ở lever cuôi
    "NAME": "Giê-su",
    "HP": 2300000,
    "STR": 400,
    "DEF": 250,
    "LUCK": 70,
    "LVL": "Chưa xác định được",
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
    "EXP": 1,
    "LVL": 1,#Bot1["EXP"]/100,
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
    "EXP": 1,
    "LVL": 34,#Bot2["EXP"]/100,
}

cacloaivukhi_MiniZombie = []
cacloaivukhi_Zombie = [""]
cacloaivukhi_BigZombie = []

print("Game này cho bạn vào một thế giới hỗn độn với Zombie ở khắp nơi bạn phải giết được Giê-su để chiến thắng(game này có thể có lỗi và chưa được tối ưu, hoàn thiện mọi command xin liên hệ Administrators: link FaceBook https://www.facebook.com/profile.php?id=100014034901974)")

vonglapcauhoi_dokho = [0]
for _ in vonglapcauhoi_dokho:
    print("Bạn hãy chọn độ khó")
    print("1. Dễ")
    print("2. khó(khi DEF của kẻ địch hơn STR của nhân vật thì kẻ địch được tăng máu)")
    traloicauhoi_dokho = input(" ")
    if traloicauhoi_dokho == "1" :
        print("Chế độ: Dễ")
    elif traloicauhoi_dokho == "2":
        print("Chế độ: Khó")
    else:
        print("Chỉ được nhập 1(Chế độ: Dễ) hoặc 2(Chế độ: Khó)")
        vonglapcauhoi_dokho.append(_)

sudunglan1_list = [0]
for _ in sudunglan1_list:

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
                player["HP"] += 1000
                player["STR"] += 1000
                player["DEF"] += 1000
                player["LUCK"] = 70
                player["CRT"] += 1000
                player["EXP"] += 1000
                player["LVL"] += 1000
                sudunglan1_list.append(0)
            else:
                sudunglan1_list.append(0)
        else:
            sudunglan1_list.append(0)


    if gioithieugame == "stats":
        print("Thông số nhân vật mặc định của bạn")
        print("HP:", player["HP"])
        print("STR:", player["STR"])
        print("DEF", player["DEF"])
        print("LUCK", player["LUCK"])
        print("CRI", player["CRT"])
        print("EXP", player["EXP"])
        print("LVL", player["LVL"])
        sudunglan1_list.append(_)

    elif gioithieugame == "play":
        print("Xin chào", NAME, ", tôi tên là:", Bot1["NAME"])
        print("Bạn là một trong những người may mắn còn sống trong trận đại dịch Zombie")
        print("Bạn phải sống sót và tập hợp những người sống sót,")
        print("đi tìm nơi ở của Giê-su Zombie, giết nó và bạn sẽ giải cứu được thế giới")
        print("Vậy bạn có đi tìm Giê-su Zombie cùng tôi không")
        print("1. Có")
        print("2. Không")

        sudunglan2_list = [0]
        for _ in sudunglan2_list:

            dichuen = input("")

            if dichuen == "1":
                print("Ở đằng kia có rất nhiều Zombie, có thể có Giê-su Zombie ở đó")
                print("1. Đi ra đó")
                print("2. Ở lại")
                dichuen = input(" ")
                if dichuen == "1":
                    soluongzombie = range(random.randint(10, 20))
                    print("Ở đó có:", max(soluongzombie) + 1, "con Zombie")
                    for slzb in soluongzombie:
                        spawn = random.randint(0, 2)
                        if spawn == 0:
                            solanlap = [0]
                            print("Thông số zombie chuẩn bị tấn công:")
                            print(MiniZombie)
                            for _ in solanlap:


                                print("Tấn công or Phòng thủ")
                                print("1. Tấn công")
                                print("2. Phòng thủ")


                                DEFtamthoiZombie = MiniZombie["DEF"] * random.randint(0, 2)
                                DEFtamthoiplayer = player["DEF"] * random.randint(0, 2)
                                DEFtamthoiBot = Bot1["DEF"] * random.randint(0, 2)


                                damageplayerlenZombiecong = player["STR"] * random.randint(1, 2) - MiniZombie["DEF"]
                                damageplayerlenZombiethu = player["STR"] * random.randint(1, 2) - DEFtamthoiZombie

                                damageBot1lenZombiecong = Bot1["STR"] * random.randint(1, 2) - MiniZombie["DEF"]
                                damageBot1lenZombiethu = Bot1["STR"] * random.randint(1, 2) - DEFtamthoiZombie

                                damageZombielenplayercong = MiniZombie["STR"] * random.randint(1, 2) - player["DEF"]
                                damageZombielenplayerthu = MiniZombie["STR"] * random.randint(1, 2) - DEFtamthoiplayer

                                damageZombielenBot1cong = MiniZombie["STR"] * random.randint(1, 2) - Bot1["DEF"]
                                damageZombielenBot1thu = MiniZombie["STR"] * random.randint(1, 2) - DEFtamthoiBot


                                LuckZombie = random.randint(MiniZombie["LUCK"], 100)
                                Luckplayer = random.randint(player["LUCK"], 100)
                                LuckBot1 = random.randint(Bot1["LUCK"], 100)


                                tancong_phongthu_player = int(input(" "))
                                tancong_phongthu_Bot1 = random.randint(0, 1)
                                tancong_phongthu_Zombie = random.randint(0, 1)

                                if damageZombielenplayercong < 0:
                                    damageZombielenplayercong = 0
                                if damageZombielenplayerthu < 0:
                                    damageZombielenplayerthu = 0
                                if damageZombielenBot1cong < 0:
                                    damageZombielenBot1cong = 0
                                if damageZombielenBot1thu < 0:
                                    damageZombielenBot1thu = 0


                                if traloicauhoi_dokho == "1":
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
                                                MiniZombie["HP"] -= damageplayerlenZombiecong
                                            if tancong_phongthu_Zombie == 1:
                                                MiniZombie["HP"] -= damageplayerlenZombiethu

                                if Bot1["HP"] > 0:
                                    if tancong_phongthu_Bot1 == 0:
                                        if LuckZombie < 80:
                                            if tancong_phongthu_Zombie == 0:
                                                MiniZombie["HP"] -= damageBot1lenZombiecong
                                            if tancong_phongthu_Zombie == 1:
                                                MiniZombie["HP"] -= damageBot1lenZombiethu

                                if tancong_phongthu_Zombie == 0:
                                    if Luckplayer < 80:
                                        if tancong_phongthu_player == 1:
                                            player["HP"] -= damageZombielenplayercong
                                        if tancong_phongthu_player == 2:
                                            player["HP"] -= damageZombielenplayerthu

                                    if LuckBot1 < 80:
                                        if tancong_phongthu_Bot1 == 0:
                                            Bot1["HP"] -= damageZombielenBot1cong
                                        if tancong_phongthu_player == 1:
                                            Bot1["HP"] -= damageZombielenBot1thu


                                if MiniZombie["HP"] < 0:
                                    MiniZombie["HP"] = 0
                                if player["HP"] < 0:
                                    player["HP"] = 0
                                if Bot1["HP"] < 0:
                                    Bot1["HP"] = 0
                                print(player)
                                if Bot1["HP"] > 0:
                                    print(Bot1)
                                print(MiniZombie)
                                if MiniZombie["HP"] == 0:
                                    print("Your kill 1 Zombie")
                                    MiniZombie["HP"] = 40
                                    MiniZombie["EXP"] += 50
                                    if MiniZombie["EXP"] > 100:
                                        MiniZombie["EXP"] = 0
                                        MiniZombie["LVL"] += 1
                                        if MiniZombie["LUCK"] < 70:
                                            loaicantang = random.randint(1, 5)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    MiniZombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    MiniZombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    MiniZombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    MiniZombie["LUCK"] += 10
                                                elif loaicantang == 5:
                                                    MiniZombie["CRT"] += 10

                                        elif MiniZombie["LUCK"] >= 70:
                                            loaicantang = random.randint(1, 4)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    MiniZombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    MiniZombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    MiniZombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    MiniZombie["LUCK"] += 10

                                    if player["HP"] > 0:
                                        player["EXP"] += 20
                                        if player["EXP"] > 100:
                                            player["LVL"] += 1
                                            print("Bạn đã lên LVL:", player["LVL"])
                                            player["EXP"] = 0
                                            if player["LUCK"] < 70:
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
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "luck":
                                                        player["LUCK"] += 10
                                                    elif loaicantang == "5" or "crt":
                                                        player["CRT"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)

                                            elif player["LUCK"] >= 70:
                                                print("Vì LUCK của bạn đã MAX nên không xuất hiện trong bảng")
                                                print("Bạn muốn tăng")
                                                print("*" * 100)
                                                print("1. HP")
                                                print("2. STR")
                                                print("3. DEF")
                                                print("4. CRT")
                                                print("*" * 100)
                                                loaicantang = input(" ")
                                                loaicantang = loaicantang.lower()
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "crt":
                                                        player["CRT"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)

                                    if Bot1["HP"] > 0:
                                        Bot1["EXP"] += 20
                                        if Bot1["EXP"] > 100:
                                            Bot1["LVL"] += 1
                                            Bot1["EXP"] = 0
                                            if Bot1["LUCK"] < 70:
                                                loaicantang = random.randint(1, 5)
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == 1:
                                                        Bot1["HP"] += 10
                                                    elif loaicantang == 2:
                                                        Bot1["STR"] += 10
                                                    elif loaicantang == 3:
                                                        Bot1["DEF"] += 10
                                                    elif loaicantang == 4:
                                                        Bot1["LUCK"] += 10
                                                    elif loaicantang == 5:
                                                        Bot1["CRT"] += 10

                                            elif Bot1["LUCK"] >= 70:
                                                loaicantang = random.randint(1, 4)
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == 1:
                                                        Bot1["HP"] += 10
                                                    elif loaicantang == 2:
                                                        Bot1["STR"] += 10
                                                    elif loaicantang == 3:
                                                        Bot1["DEF"] += 10
                                                    elif loaicantang == 4:
                                                        Bot1["LUCK"] += 10
                                else:
                                    solanlap.append(_)


                                Bot1chetgoc = [0]
                                Bot1chetsosanh = [0]
                                if Bot1chetgoc == Bot1chetsosanh:
                                    if Bot1["HP"] == 0:
                                        print("Bạn hãy cố gắng giải cứu thế giới")
                                        print("VĨNH BIỆT!!!")
                                        print(Bot1["NAME"], ": DIE")
                                        Bot1chetsosanh[0] = 1

                                if player["HP"] == 0:
                                    print("Your die")
                                    print("GAME OVER")
                                    print("Nếu muốn chơi lại hãy nhập (replay)")
                                    choilai = input("")
                                    if choilai == "replay":
                                        sudunglan1_list.append(_)




                                else:
                                    solanlap.append(_)


                        elif spawn == 1:
                            solanlap = [0]
                            print("Thông số zombie chuẩn bị tấn công:")
                            print(Zombie)
                            for _ in solanlap:


                                print("Tấn công or Phòng thủ")
                                print("1. Tấn công")
                                print("2. Phòng thủ")


                                DEFtamthoiZombie = Zombie["DEF"] * random.randint(0, 2)
                                DEFtamthoiplayer = player["DEF"] * random.randint(0, 2)
                                DEFtamthoiBot = Bot1["DEF"] * random.randint(0, 2)


                                damageplayerlenZombiecong = player["STR"] - Zombie["DEF"]
                                damageplayerlenZombiethu = player["STR"] - DEFtamthoiZombie

                                damageBot1lenZombiecong = Bot1["STR"] - Zombie["DEF"]
                                damageBot1lenZombiethu = Bot1["STR"] - DEFtamthoiZombie

                                damageZombielenplayercong = Zombie["STR"] - player["DEF"]
                                damageZombielenplayerthu = Zombie["STR"] - DEFtamthoiplayer

                                damageZombielenBot1cong = Zombie["STR"] - Bot1["DEF"]
                                damageZombielenBot1thu = Zombie["STR"] - DEFtamthoiBot


                                LuckZombie = random.randint(Zombie["LUCK"], 100)
                                Luckplayer = random.randint(player["LUCK"], 100)
                                LuckBot1 = random.randint(Bot1["LUCK"], 100)


                                tancong_phongthu_player = int(input(" "))
                                tancong_phongthu_Bot1 = random.randint(0, 1)
                                tancong_phongthu_Zombie = random.randint(0, 1)


                                if damageZombielenplayercong < 0:
                                    damageZombielenplayercong = 0
                                if damageZombielenplayerthu < 0:
                                    damageZombielenplayerthu = 0
                                if damageZombielenBot1cong < 0:
                                    damageZombielenBot1cong = 0
                                if damageZombielenBot1thu < 0:
                                    damageZombielenBot1thu = 0

                                if traloicauhoi_dokho == "1":
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
                                                Zombie["HP"] -= damageplayerlenZombiecong
                                            if tancong_phongthu_Zombie == 1:
                                                Zombie["HP"] -= damageplayerlenZombiethu

                                if Bot1["HP"] > 0:
                                    if tancong_phongthu_Bot1 == 0:
                                        if LuckZombie < 80:
                                            if tancong_phongthu_Zombie == 0:
                                                Zombie["HP"] -= damageBot1lenZombiecong
                                            if tancong_phongthu_Zombie == 1:
                                                Zombie["HP"] -= damageBot1lenZombiethu

                                if tancong_phongthu_Zombie == 0:
                                    if Luckplayer < 80:
                                        if tancong_phongthu_player == 1:
                                            player["HP"] -= damageZombielenplayercong
                                        if tancong_phongthu_player == 2:
                                            player["HP"] -= damageZombielenplayerthu

                                    if LuckBot1 < 80:
                                        if tancong_phongthu_Bot1 == 1:
                                            Bot1["HP"] -= damageZombielenBot1cong
                                        if tancong_phongthu_Bot1 == 2:
                                            Bot1["HP"] -= damageZombielenBot1thu


                                if Zombie["HP"] < 0:
                                    Zombie["HP"] = 0
                                if player["HP"] < 0:
                                    player["HP"] = 0
                                if Bot1["HP"] < 0:
                                    Bot1["HP"] = 0
                                print(player)
                                if Bot1["HP"] > 0:
                                    print(Bot1)
                                print(Zombie)
                                if Zombie["HP"] == 0:
                                    print("Your kill 1 Zombie")
                                    Zombie["HP"] = 80
                                    Zombie["EXP"] += 50
                                    if Zombie["EXP"] > 100:
                                        Zombie["LVL"] += 1
                                        if Zombie["LUCK"] < 70:
                                            loaicantang = random.randint(1, 5)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    Zombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    Zombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    Zombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    Zombie["LUCK"] += 10
                                                elif loaicantang == 5:
                                                    Zombie["CRT"] += 10

                                        elif Zombie["LUCK"] >= 70:
                                            loaicantang = random.randint(1, 4)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    Zombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    Zombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    Zombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    Zombie["LUCK"] += 10

                                    if player["HP"] > 0:
                                        player["EXP"] += 20
                                        if player["EXP"] > 100:
                                            player["LVL"] += 1
                                            print("Bạn đã lên LVL:", player["LVL"])
                                            player["EXP"] = 0
                                            if player["LUCK"] < 70:
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
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "luck":
                                                        player["LUCK"] += 10
                                                    elif loaicantang == "5" or "crt":
                                                        player["CRT"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)

                                            elif player["LUCK"] >= 70:
                                                print("Vì LUCK của bạn đã MAX nên không xuất hiện trong bảng")
                                                print("Bạn muốn tăng")
                                                print("*" * 100)
                                                print("1. HP")
                                                print("2. STR")
                                                print("3. DEF")
                                                print("4. CRT")
                                                print("*" * 100)
                                                loaicantang = input(" ")
                                                loaicantang = loaicantang.lower()
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "crt":
                                                        player["LUCK"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)


                                    if Bot1["HP"] > 0:
                                        Bot1["EXP"] += 20
                                        if Bot1["EXP"] > 100:
                                            Bot1["LVL"] += 1
                                            Bot1["EXP"] = 0
                                            if Bot1["LUCK"] < 70:
                                                loaicantang = random.randint(1, 5)
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == 1:
                                                        Bot1["HP"] += 10
                                                    elif loaicantang == 2:
                                                        Bot1["STR"] += 10
                                                    elif loaicantang == 3:
                                                        Bot1["DEF"] += 10
                                                    elif loaicantang == 4:
                                                        Bot1["LUCK"] += 10
                                                    elif loaicantang == 5:
                                                        Bot1["CRT"] += 10

                                            elif Bot1["LUCK"] >= 70:
                                                loaicantang = random.randint(1, 4)
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == 1:
                                                        Bot1["HP"] += 10
                                                    elif loaicantang == 2:
                                                        Bot1["STR"] += 10
                                                    elif loaicantang == 3:
                                                        Bot1["DEF"] += 10
                                                    elif loaicantang == 4:
                                                        Bot1["LUCK"] += 10



                                else:
                                    solanlap.append(_)

                                Bot1chetgoc = [0]
                                Bot1chetsosanh = [0]
                                if Bot1chetgoc == Bot1chetsosanh:
                                    if Bot1["HP"] == 0:
                                        print("Bạn hãy cố gắng giải cứu thế giới")
                                        print("VĨNH BIỆT!!!")
                                        print(Bot1["NAME"], ": DIE")
                                        Bot1chetsosanh.append(0)

                                if player["HP"] == 0:
                                    print("Your die")
                                    print("GAME OVER")
                                    print("Nếu muốn chơi lại hãy nhập (replay)")
                                    choilai = input("")
                                    if choilai == "replay":
                                        sudunglan1_list.append(_)


                        elif spawn == 2:
                            solanlap = [0]
                            print("Thông số zombie chuẩn bị tấn công:")
                            print(BigZombie)
                            for _ in solanlap:

                                print("Tấn công or Phòng thủ")
                                print("1. Tấn công")
                                print("2. Phòng thủ")

                                DEFtamthoiZombie = BigZombie["DEF"] * random.randint(0, 2)
                                DEFtamthoiplayer = player["DEF"] * random.randint(0, 2)
                                DEFtamthoiBot = Bot1["DEF"] * random.randint(0, 2)

                                damageplayerlenZombiecong = player["STR"] - BigZombie["DEF"]
                                damageplayerlenZombiethu = player["STR"] - DEFtamthoiZombie

                                damageBot1lenZombiecong = Bot1["STR"] - BigZombie["DEF"]
                                damageBot1lenZombiethu = Bot1["STR"] - DEFtamthoiZombie

                                damageZombielenplayercong = BigZombie["STR"] - player["DEF"]
                                damageZombielenplayerthu = BigZombie["STR"] - DEFtamthoiplayer

                                damageZombielenBot1cong = BigZombie["STR"] - Bot1["DEF"]
                                damageZombielenBot1thu = BigZombie["STR"] - DEFtamthoiBot

                                LuckZombie = random.randint(BigZombie["LUCK"], 100)
                                Luckplayer = random.randint(player["LUCK"], 100)
                                LuckBot1 = random.randint(Bot1["LUCK"], 100)

                                tancong_phongthu_player = int(input(" "))
                                tancong_phongthu_Bot1 = random.randint(0, 1)
                                tancong_phongthu_Zombie = random.randint(0, 1)

                                if damageZombielenplayercong < 0:
                                    damageZombielenplayercong = 0
                                if damageZombielenplayerthu < 0:
                                    damageZombielenplayerthu = 0
                                if damageZombielenBot1cong < 0:
                                    damageZombielenBot1cong = 0
                                if damageZombielenBot1thu < 0:
                                    damageZombielenBot1thu = 0

                                if traloicauhoi_dokho == "1":
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
                                                BigZombie["HP"] -= damageplayerlenZombiecong
                                            if tancong_phongthu_Zombie == 1:
                                                BigZombie["HP"] -= damageplayerlenZombiethu

                                if Bot1["HP"] > 0:
                                    if tancong_phongthu_Bot1 == 0:
                                        if LuckZombie < 80:
                                            if tancong_phongthu_Zombie == 0:
                                                BigZombie["HP"] -= damageBot1lenZombiecong
                                            if tancong_phongthu_Zombie == 1:
                                                Zombie["HP"] -= damageBot1lenZombiethu

                                if tancong_phongthu_Zombie == 0:
                                    if Luckplayer < 80:
                                        if tancong_phongthu_player == 1:
                                            player["HP"] -= damageZombielenplayercong
                                        if tancong_phongthu_player == 2:
                                            player["HP"] -= damageZombielenplayerthu

                                    if LuckBot1 < 80:
                                        if tancong_phongthu_player == 1:
                                            Bot1["HP"] -= damageZombielenplayercong
                                        if tancong_phongthu_player == 2:
                                            Bot1["HP"] -= damageZombielenplayerthu

                                if BigZombie["HP"] < 0:
                                    BigZombie["HP"] = 0
                                if player["HP"] < 0:
                                    player["HP"] = 0
                                if Bot1["HP"] < 0:
                                    Bot1["HP"] = 0
                                print(player)
                                if Bot1["HP"] > 0:
                                    print(Bot1)
                                print(BigZombie)
                                if BigZombie["HP"] == 0:
                                    print("Your kill 1 Zombie")
                                    BigZombie["HP"] = 160
                                    BigZombie["EXP"] += 50
                                    if BigZombie["EXP"] > 100:
                                        BigZombie["LVL"] += 1
                                        if BigZombie["LUCK"] < 70:
                                            loaicantang = random.randint(1, 5)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    BigZombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    BigZombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    BigZombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    BigZombie["LUCK"] += 10
                                                elif loaicantang == 5:
                                                    BigZombie["CRT"] += 10

                                        elif BigZombie["LUCK"] >= 70:
                                            loaicantang = random.randint(1, 4)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    BigZombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    BigZombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    BigZombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    BigZombie["LUCK"] += 10

                                    if player["HP"] > 0:
                                        player["EXP"] += 20
                                        if player["EXP"] > 100:
                                            player["LVL"] += 1
                                            print("Bạn đã lên LVL:", player["LVL"])
                                            player["EXP"] = 0
                                            if player["LUCK"] < 70:
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
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "luck":
                                                        player["LUCK"] += 10
                                                    elif loaicantang == "5" or "crt":
                                                        player["CRT"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)

                                            elif player["LUCK"] >= 70:
                                                print("Vì LUCK của bạn đã MAX nên không xuất hiện trong bảng")
                                                print("Bạn muốn tăng")
                                                print("*" * 100)
                                                print("1. HP")
                                                print("2. STR")
                                                print("3. DEF")
                                                print("4. CRT")
                                                print("*" * 100)
                                                loaicantang = input(" ")
                                                loaicantang = loaicantang.lower()
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "crt":
                                                        player["LUCK"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)


                                        if Bot1["HP"] > 0:
                                            Bot1["EXP"] += 20
                                            if Bot1["EXP"] > 100:
                                                Bot1["LVL"] += 1
                                                Bot1["EXP"] = 0
                                                if Bot1["LUCK"] < 70:
                                                    loaicantang = random.randint(1, 5)
                                                    sudunglan3_list = [0]
                                                    for _ in sudunglan3_list:
                                                        if loaicantang == 1:
                                                            Bot1["HP"] += 10
                                                        elif loaicantang == 2:
                                                            Bot1["STR"] += 10
                                                        elif loaicantang == 3:
                                                            Bot1["DEF"] += 10
                                                        elif loaicantang == 4:
                                                            Bot1["LUCK"] += 10
                                                        elif loaicantang == 5:
                                                            Bot1["CRT"] += 10

                                                elif Bot1["LUCK"] >= 70:
                                                    loaicantang = random.randint(1, 4)
                                                    sudunglan3_list = [0]
                                                    for _ in sudunglan3_list:
                                                        if loaicantang == 1:
                                                            Bot1["HP"] += 10
                                                        elif loaicantang == 2:
                                                            Bot1["STR"] += 10
                                                        elif loaicantang == 3:
                                                            Bot1["DEF"] += 10
                                                        elif loaicantang == 4:
                                                            Bot1["LUCK"] += 10



                                else:
                                    solanlap.append(_)

                                Bot1chetgoc = [0]
                                Bot1chetsosanh = [0]
                                if Bot1chetgoc == Bot1chetsosanh:
                                    if Bot1["HP"] == 0:
                                        print("Bạn hãy cố gắng giải cứu thế giới")
                                        print("VĨNH BIỆT!!!")
                                        print(Bot1["NAME"], ": DIE")
                                        Bot1chetsosanh.append(0)

                                if player["HP"] == 0:
                                    print("Your die")
                                    print("GAME OVER")
                                    print("Nếu muốn chơi lại hãy nhập (replay)")
                                    choilai = input("")
                                    if choilai == "replay":
                                        sudunglan1_list.append(_)


                elif dichuen == "2":
                    print("Vì bạn đã đi ra khỏi nơi an toàn nên có rất nhiều Zombie xung quanh bạn bạn")
                    soluongzombie = range(random.randint(10, 20))
                    print("Quanh bạn có:", max(soluongzombie) + 1, "con Zombie")
                    for slzb in soluongzombie:
                        spawn = random.randint(0, 2)
                        if spawn == 0:
                            solanlap = [0]
                            print("Thông số zombie chuẩn bị tấn công:")
                            print(MiniZombie)
                            for _ in solanlap:

                                print("Tấn công or Phòng thủ")
                                print("1. Tấn công")
                                print("2. Phòng thủ")

                                DEFtamthoiZombie = MiniZombie["DEF"] * random.randint(0, 2)
                                DEFtamthoiplayer = player["DEF"] * random.randint(0, 2)

                                damageplayerlenZombiecong = player["STR"] - MiniZombie["DEF"]
                                damageplayerlenZombiethu = player["STR"] - DEFtamthoiZombie

                                damageZombielenplayercong = MiniZombie["STR"] - player["DEF"]
                                damageZombielenplayerthu = MiniZombie["STR"] - DEFtamthoiplayer


                                LuckZombie = random.randint(MiniZombie["LUCK"], 100)
                                Luckplayer = random.randint(player["LUCK"], 100)

                                tancong_phongthu_player = int(input(" "))
                                tancong_phongthu_Zombie = random.randint(0, 1)

                                if damageZombielenplayercong < 0:
                                    damageZombielenplayercong = 0
                                if damageZombielenplayerthu < 0:
                                    damageZombielenplayerthu = 0

                                if traloicauhoi_dokho == "1":
                                    if damageplayerlenZombiecong < 0:
                                        damageplayerlenZombiecong = 0
                                    if damageplayerlenZombiethu < 0:
                                        damageplayerlenZombiethu = 0


                                if tancong_phongthu_player == 1:
                                    if LuckZombie < 80:
                                        if tancong_phongthu_Zombie == 0:
                                            MiniZombie["HP"] -= damageplayerlenZombiecong
                                        if tancong_phongthu_Zombie == 1:
                                            MiniZombie["HP"] -= damageplayerlenZombiethu


                                if tancong_phongthu_Zombie == 0:
                                    if Luckplayer < 80:
                                        if tancong_phongthu_player == 1:
                                            player["HP"] -= damageZombielenplayercong
                                        if tancong_phongthu_player == 2:
                                            player["HP"] -= damageZombielenplayerthu


                                if MiniZombie["HP"] < 0:
                                    MiniZombie["HP"] = 0
                                if player["HP"] < 0:
                                    player["HP"] = 0
                                print(player)
                                print(MiniZombie)
                                if MiniZombie["HP"] == 0:
                                    print("Your kill 1 Zombie")
                                    MiniZombie["HP"] = 40
                                    MiniZombie["EXP"] += 50
                                    if MiniZombie["EXP"] > 100:
                                        MiniZombie["LVL"] += 1
                                        if MiniZombie["LUCK"] < 70:
                                            loaicantang = random.randint(1, 5)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    MiniZombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    MiniZombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    MiniZombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    MiniZombie["LUCK"] += 10
                                                elif loaicantang == 5:
                                                    MiniZombie["CRT"] += 10

                                        elif MiniZombie["LUCK"] >= 70:
                                            loaicantang = random.randint(1, 4)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    MiniZombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    MiniZombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    MiniZombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    MiniZombie["LUCK"] += 10

                                    if player["HP"] > 0:
                                        player["EXP"] += 20
                                        if player["EXP"] > 100:
                                            player["LVL"] += 1
                                            print("Bạn đã lên LVL:", player["LVL"])
                                            player["EXP"] = 0
                                            if player["LUCK"] < 70:
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
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "luck":
                                                        player["LUCK"] += 10
                                                    elif loaicantang == "5" or "crt":
                                                        player["CRT"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)

                                            elif player["LUCK"] >= 70:
                                                print("Vì LUCK của bạn đã MAX nên không xuất hiện trong bảng")
                                                print("Bạn muốn tăng")
                                                print("*" * 100)
                                                print("1. HP")
                                                print("2. STR")
                                                print("3. DEF")
                                                print("4. CRT")
                                                print("*" * 100)
                                                loaicantang = input(" ")
                                                loaicantang = loaicantang.lower()
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "crt":
                                                        player["LUCK"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)



                                elif player["HP"] == 0:
                                    print("Your die")
                                    print("GAME OVER")
                                    print("Nếu muốn chơi lại hãy nhập (replay)")
                                    choilai = input("")
                                    if choilai == "replay":
                                        sudunglan1_list.append(_)

                                else:
                                    solanlap.append(_)


                        elif spawn == 1:
                            solanlap = [0]
                            print("Thông số zombie chuẩn bị tấn công:")
                            print(Zombie)
                            for _ in solanlap:

                                print("Tấn công or Phòng thủ")
                                print("1. Tấn công")
                                print("2. Phòng thủ")

                                DEFtamthoiZombie = Zombie["DEF"] * random.randint(0, 2)
                                DEFtamthoiplayer = player["DEF"] * random.randint(0, 2)

                                damageplayerlenZombiecong = player["STR"] - Zombie["DEF"]
                                damageplayerlenZombiethu = player["STR"] - DEFtamthoiZombie

                                damageZombielenplayercong = Zombie["STR"] - player["DEF"]
                                damageZombielenplayerthu = Zombie["STR"] - DEFtamthoiplayer

                                LuckZombie = random.randint(Zombie["LUCK"], 100)
                                Luckplayer = random.randint(player["LUCK"], 100)

                                tancong_phongthu_player = int(input(" "))
                                tancong_phongthu_Zombie = random.randint(0, 1)

                                if damageZombielenplayercong < 0:
                                    damageZombielenplayercong = 0
                                if damageZombielenplayerthu < 0:
                                    damageZombielenplayerthu = 0

                                if traloicauhoi_dokho == "1":
                                    if damageplayerlenZombiecong < 0:
                                        damageplayerlenZombiecong = 0
                                    if damageplayerlenZombiethu < 0:
                                        damageplayerlenZombiethu = 0

                                if tancong_phongthu_player == 1:
                                    if LuckZombie < 80:
                                        if tancong_phongthu_Zombie == 0:
                                            Zombie["HP"] -= damageplayerlenZombiecong
                                        if tancong_phongthu_Zombie == 1:
                                            Zombie["HP"] -= damageplayerlenZombiethu

                                if tancong_phongthu_Zombie == 0:
                                    if Luckplayer < 80:
                                        if tancong_phongthu_player == 1:
                                            player["HP"] -= damageZombielenplayercong
                                        if tancong_phongthu_player == 2:
                                            player["HP"] -= damageZombielenplayerthu

                                if Zombie["HP"] < 0:
                                    MiniZombie["HP"] = 0
                                if player["HP"] < 0:
                                    player["HP"] = 0
                                print(player)
                                print(Zombie)
                                if Zombie["HP"] == 0:
                                    print("Your kill 1 Zombie")
                                    Zombie["HP"] = 40
                                    Zombie["EXP"] += 50
                                    if Zombie["EXP"] > 100:
                                        Zombie["EXP"] = 0
                                        Zombie["LVL"] += 1
                                        if Zombie["LUCK"] < 70:
                                            loaicantang = random.randint(1, 5)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    Zombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    Zombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    Zombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    Zombie["LUCK"] += 10
                                                elif loaicantang == 5:
                                                    Zombie["CRT"] += 10

                                        elif Zombie["LUCK"] >= 70:
                                            loaicantang = random.randint(1, 4)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    Zombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    Zombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    Zombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    Zombie["LUCK"] += 10

                                    if player["HP"] > 0:
                                        player["EXP"] += 20
                                        if player["EXP"] > 100:
                                            player["EXP"] = 0
                                            player["LVL"] += 1
                                            print("Bạn đã lên LVL:", player["LVL"])
                                            player["EXP"] = 0
                                            if player["LUCK"] < 70:
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
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "luck":
                                                        player["LUCK"] += 10
                                                    elif loaicantang == "5" or "crt":
                                                        player["CRT"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)

                                            elif player["LUCK"] >= 70:
                                                print("Vì LUCK của bạn đã MAX nên không xuất hiện trong bảng")
                                                print("Bạn muốn tăng")
                                                print("*" * 100)
                                                print("1. HP")
                                                print("2. STR")
                                                print("3. DEF")
                                                print("4. CRT")
                                                print("*" * 100)
                                                loaicantang = input(" ")
                                                loaicantang = loaicantang.lower()
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "crt":
                                                        player["LUCK"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)



                                elif player["HP"] == 0:
                                    print("Your die")
                                    print("GAME OVER")
                                    print("Nếu muốn chơi lại hãy nhập (replay)")
                                    choilai = input("")
                                    if choilai == "replay":
                                        sudunglan1_list.append(_)

                                else:
                                    solanlap.append(_)


                        elif spawn == 2:
                            solanlap = [0]
                            print("Thông số zombie chuẩn bị tấn công:")
                            print(BigZombie)
                            for _ in solanlap:

                                print("Tấn công or Phòng thủ")
                                print("1. Tấn công")
                                print("2. Phòng thủ")

                                DEFtamthoiZombie = BigZombie["DEF"] * random.randint(0, 2)
                                DEFtamthoiplayer = player["DEF"] * random.randint(0, 2)

                                damageplayerlenZombiecong = player["STR"] - BigZombie["DEF"]
                                damageplayerlenZombiethu = player["STR"] - DEFtamthoiZombie

                                damageZombielenplayercong = BigZombie["STR"] - player["DEF"]
                                damageZombielenplayerthu = BigZombie["STR"] - DEFtamthoiplayer

                                LuckZombie = random.randint(BigZombie["LUCK"], 100)
                                Luckplayer = random.randint(player["LUCK"], 100)

                                tancong_phongthu_player = int(input(" "))
                                tancong_phongthu_Zombie = random.randint(0, 1)

                                if damageZombielenplayercong < 0:
                                    damageZombielenplayercong = 0
                                if damageZombielenplayerthu < 0:
                                    damageZombielenplayerthu = 0

                                if traloicauhoi_dokho == "1":
                                    if damageplayerlenZombiecong < 0:
                                        damageplayerlenZombiecong = 0
                                    if damageplayerlenZombiethu < 0:
                                        damageplayerlenZombiethu = 0

                                if tancong_phongthu_player == 1:
                                    if LuckZombie < 80:
                                        if tancong_phongthu_Zombie == 0:
                                            BigZombie["HP"] -= damageplayerlenZombiecong
                                        if tancong_phongthu_Zombie == 1:
                                            BigZombie["HP"] -= damageplayerlenZombiethu

                                if tancong_phongthu_Zombie == 0:
                                    if Luckplayer < 80:
                                        if tancong_phongthu_player == 1:
                                            player["HP"] -= damageZombielenplayercong
                                        if tancong_phongthu_player == 2:
                                            player["HP"] -= damageZombielenplayerthu

                                if BigZombie["HP"] < 0:
                                    MiniZombie["HP"] = 0
                                if player["HP"] < 0:
                                    player["HP"] = 0
                                print(player)
                                print(BigZombie)
                                if BigZombie["HP"] == 0:
                                    print("Your kill 1 Zombie")
                                    BigZombie["HP"] = 160
                                    BigZombie["EXP"] += 50
                                    if BigZombie["EXP"] > 100:
                                        BigZombie["EXP"] = 0
                                        BigZombie["LVL"] += 1
                                        if Zombie["LUCK"] < 70:
                                            loaicantang = random.randint(1, 5)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    BigZombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    BigZombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    BigZombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    BigZombie["LUCK"] += 10
                                                elif loaicantang == 5:
                                                    BigZombie["CRT"] += 10

                                        elif BigZombie["LUCK"] >= 70:
                                            loaicantang = random.randint(1, 4)
                                            sudunglan3_list = [0]
                                            for _ in sudunglan3_list:
                                                if loaicantang == 1:
                                                    BigZombie["HP"] += 10
                                                elif loaicantang == 2:
                                                    BigZombie["STR"] += 10
                                                elif loaicantang == 3:
                                                    BigZombie["DEF"] += 10
                                                elif loaicantang == 4:
                                                    BigZombie["LUCK"] += 10

                                    if player["HP"] > 0:
                                        player["EXP"] += 20
                                        if player["EXP"] > 100:
                                            player["EXP"] = 0
                                            player["LVL"] += 1
                                            print("Bạn đã lên LVL:", player["LVL"])
                                            player["EXP"] = 0
                                            if player["LUCK"] < 70:
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
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "luck":
                                                        player["LUCK"] += 10
                                                    elif loaicantang == "5" or "crt":
                                                        player["CRT"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)

                                            elif player["LUCK"] >= 70:
                                                print("Vì LUCK của bạn đã MAX nên không xuất hiện trong bảng")
                                                print("Bạn muốn tăng")
                                                print("*" * 100)
                                                print("1. HP")
                                                print("2. STR")
                                                print("3. DEF")
                                                print("4. CRT")
                                                print("*" * 100)
                                                loaicantang = input(" ")
                                                loaicantang = loaicantang.lower()
                                                sudunglan3_list = [0]
                                                for _ in sudunglan3_list:
                                                    if loaicantang == "1" or "hp":
                                                        player["HP"] += 10
                                                    elif loaicantang == "2" or "str":
                                                        player["STR"] += 10
                                                    elif loaicantang == "3" or "def":
                                                        player["DEF"] += 10
                                                    elif loaicantang == "4" or "crt":
                                                        player["LUCK"] += 10
                                                    else:
                                                        print("Bạn không có thông số:", loaicantang)
                                                        print("Bạn hãy nhập lại")
                                                        sudunglan3_list.append(_)

                                elif player["HP"] == 0:
                                    print("Your die")
                                    print("GAME OVER")
                                    print("Nếu muốn chơi lại hãy nhập (replay)")
                                    choilai = input("")
                                    if choilai == "replay":
                                        sudunglan1_list.append(_)

                                else:
                                    solanlap.append(_)


            elif dichuen == "2":
                print("Bạn ở lại một mình và chết đói vì không có thức ăn")
                print("GAME OVER")
                print("Nếu muốn chơi lại hãy nhập (replay)")
                choilai = input(" ")
                choilai = choilai.lower()
                if choilai == "replay":
                    sudunglan1_list.append(_)
            else:
                print("Tôi không hiểu ý bạn, bạn hãy trả lời lại")
                sudunglan2_list.append(_)

    else:
        if gioithieugame != "cmd_hack":
            print("Command của bạn không có trong từ điển của chúng tôi")
            print("Xin bạn hãy nhập lại")
        sudunglan1_list.append(_)






