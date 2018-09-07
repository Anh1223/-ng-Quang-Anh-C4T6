def cottruyen(nameplayer, nameBot1, loai_Zombie):
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
                    player["HP"] += 1000
                    player["STR"] += 1000
                    player["DEF"] += 1000
                    player["LUCK"] = 70
                    player["CRT"] += 1000
                    player["EXP"] += 1000
                    player["LVL"] += 1000

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

            sudunglan2_list = [0]
            for _ in sudunglan2_list:

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
                            tinh_combat(nameplayer, nameBot1, loai_Zombie[spawn], traloicauhoi_dokho)
                    elif dichuen == "2":
                        print("Vì bạn đã đi ra khỏi nơi an toàn nên có rất nhiều Zombie xung quanh bạn bạn")
                        soluongzombie = range(randint(10, 20))
                        print("Quanh bạn có:", max(soluongzombie) + 1, "con Zombie")
                        for slzb in soluongzombie:
                            spawn = randint(0, 2)
                            tinh_combat_khongcoBot(nameplayer, loai_Zombie[spawn], traloicauhoi_dokho)


                elif dichuen == "2":
                    while True:
                        print("Bạn ở lại một mình và chết đói vì không có thức ăn")
                        print("GAME OVER")
                        while True:
                            print("Nếu muốn chơi lại hãy nhập (replay)")
                            choilai = input(" ")
                            choilai = choilai.lower()
                            if choilai == "replay":
                                cottruyen(nameplayer, nameBot1, loai_Zombie)
                                break
                            else:
                                print("Xin nhập lại")

                else:
                    print("Tôi không hiểu ý bạn, bạn hãy trả lời lại")


        else:
            if gioithieugame != "cmd_hack":
                print("Command của bạn không có trong từ điển của chúng tôi")
                print("Xin bạn hãy nhập lại")