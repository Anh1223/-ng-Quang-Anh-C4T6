def tinh_combat(nameplayer, nameBot1, nameZombie, traloicauhoi_dokho):
    print("Thông số zombie chuẩn bị tấn công:")
    print(nameZombie)
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
            nameZombie["HP"] = 40
            nameZombie["EXP"] += 50
            if nameZombie["EXP"] > 100:
                nameZombie["EXP"] = 0
                nameZombie["LVL"] += 1
                if nameZombie["LUCK"] < 70:
                    loaicantang = randint(1, 5)
                    if loaicantang == 1:
                        nameZombie["HP"] += 10
                    elif loaicantang == 2:
                        nameZombie["STR"] += 10
                    elif loaicantang == 3:
                        nameZombie["DEF"] += 10
                    elif loaicantang == 4:
                        nameZombie["LUCK"] += 10
                    elif loaicantang == 5:
                        nameZombie["CRT"] += 10

                elif nameZombie["LUCK"] >= 70:
                    loaicantang = randint(1, 4)
                    if loaicantang == 1:
                        nameZombie["HP"] += 10
                    elif loaicantang == 2:
                        nameZombie["STR"] += 10
                    elif loaicantang == 3:
                        nameZombie["DEF"] += 10
                    elif loaicantang == 4:
                        nameZombie["LUCK"] += 10

            if Bot1chetgoc == Bot1chetsosanh:
                if nameBot1["HP"] == 0:
                    print("Bạn hãy cố gắng giải cứu thế giới")
                    print("VĨNH BIỆT!!!")
                    print(nameBot1["NAME"], ": DIE")
                    Bot1chetsosanh.append(1)

            if nameplayer["HP"] > 0:
                nameplayer["EXP"] += 20
                if nameplayer["EXP"] > 100:
                    nameplayer["LVL"] += 1
                    print("Bạn đã lên LVL:", nameplayer["LVL"])
                    nameplayer["EXP"] = 0
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

            if nameBot1["HP"] > 0:
                nameBot1["EXP"] += 20
                if nameBot1["EXP"] > 100:
                    nameBot1["LVL"] += 1
                    nameBot1["EXP"] = 0
                    if nameBot1["LUCK"] < 70:
                        loaicantang = randint(1, 5)
                        if loaicantang == 1:
                            nameBot1["HP"] += 10
                        elif loaicantang == 2:
                            nameBot1["STR"] += 10
                        elif loaicantang == 3:
                            nameBot1["DEF"] += 10
                        elif loaicantang == 4:
                            nameBot1["LUCK"] += 10
                        elif loaicantang == 5:
                            nameBot1["CRT"] += 10

                    elif nameBot1["LUCK"] >= 70:
                        loaicantang = randint(1, 4)
                        if loaicantang == 1:
                            nameBot1["HP"] += 10
                        elif loaicantang == 2:
                            nameBot1["STR"] += 10
                        elif loaicantang == 3:
                            nameBot1["DEF"] += 10
                        elif loaicantang == 4:
                            nameBot1["CRT"] += 10
            break

        if nameplayer["HP"] == 0:
            print("Your die")
            while True:
                print("Nếu muốn chơi lại hãy nhập (replay)")
                choilai = input(" ")
                choilai = choilai.lower()
                if choilai == "replay":
                    cottruyen()
                    break
                else:
                    print("Xin nhập lại")

def tinh_combat_khongcoBot(nameplayer, nameZombie, traloicauhoi_dokho):
    print("Thông số zombie chuẩn bị tấn công:")
    print(nameZombie)
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
        if damageZombielenBot1cong < 0:
            damageZombielenBot1cong = 0
        if damageZombielenBot1thu < 0:
            damageZombielenBot1thu = 0

        if traloicauhoi_dokho == "1":
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
            nameZombie["HP"] = 40
            nameZombie["EXP"] += 50
            if nameZombie["EXP"] > 100:
                nameZombie["EXP"] = 0
                nameZombie["LVL"] += 1
                if nameZombie["LUCK"] < 70:
                    loaicantang = randint(1, 5)
                    if loaicantang == 1:
                        nameZombie["HP"] += 10
                    elif loaicantang == 2:
                        nameZombie["STR"] += 10
                    elif loaicantang == 3:
                        nameZombie["DEF"] += 10
                    elif loaicantang == 4:
                        nameZombie["LUCK"] += 10
                    elif loaicantang == 5:
                        nameZombie["CRT"] += 10

                elif nameZombie["LUCK"] >= 70:
                    loaicantang = randint(1, 4)
                    if loaicantang == 1:
                        nameZombie["HP"] += 10
                    elif loaicantang == 2:
                        nameZombie["STR"] += 10
                    elif loaicantang == 3:
                        nameZombie["DEF"] += 10
                    elif loaicantang == 4:
                        nameZombie["LUCK"] += 10

            if nameplayer["HP"] > 0:
                nameplayer["EXP"] += 20
                if nameplayer["EXP"] > 100:
                    nameplayer["LVL"] += 1
                    print("Bạn đã lên LVL:", nameplayer["LVL"])
                    nameplayer["EXP"] = 0
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

            break

        if nameplayer["HP"] == 0:
            print("Your die")
            while True:
                print("Nếu muốn chơi lại hãy nhập (replay)")
                choilai = input(" ")
                choilai = choilai.lower()
                if choilai == "replay":
                    cottruyen()
                    break
                else:
                    print("Xin nhập lại")