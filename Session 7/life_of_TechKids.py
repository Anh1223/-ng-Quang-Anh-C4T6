Orc = {
    "NAME": "MiniOrc",
    "CLASS": "Orc",
    "HP": 20,
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
    "DEF": 4,
    "LUCK": 10,
    "AGI": 2,
    "LVL": 1,
}
while True:
    cmd = input("Your command(Stats or Here)")
    cmd = cmd.lower()
    if cmd == "stats":
        print("YOUR NAME:", player["NAME"])
        print("CLASS:", player["CLASS"])
        print("HP", player["HP"])
        print("STR", player["STR"])
        print("DEF", player["DEF"])
        print("LUCK", player["LUCK"])
        print("AGI", player["AGI"])
        print("LVL", player["LVL"])
    elif cmd == "here":
        print("Bạn đang ở trước cửa TechKids")
        print("Bạn có 2 lựa chọn")
        print("1. Về TechKids")
        print("2. Đi vào khu rừng phía trước")
        option = input("Lựa chọn của bạn ?")
        if option == "1":
            print("Xin lỗi, đã hết giờ làm việc")
        elif option == "2":
            print("Bạn đã bước vào rừng")
            print("Bạn thấy một bình thủy dịch ở trên mặt đất")
            print("1. Bỏ qua")
            print("2. Nhặt lên sử dụng")
            option = input("Lựa chọn bạn")
            if option == "1":
                print("Tiếc quá")
                print("Bạn gặp 1 con Orc")
                print("1. Chạy ra khỏi khu vực này")
                print("2. Nấp vào hang đá bên cạnh")
                print("3. ĐÁNH!!!")
                option = input("Lựa chọn của bạn?")
                if option == "1":
                    print("Do bạn chạy quá chậm nên đã bị Orc bắt đi")
                elif option == "2":
                    print("Con Orc không nhìn thấy")
                    print("Tuy nhiên bạn quay lại nhìn vào trong hanh, bạn thấy một đoàn sói")
                elif option == "3":
                    print("OPPONENT")
                    print(Orc)
                    solanlap = [0]
                    for _ in solanlap:
                        damageplayer = player["STR"] - Orc["DEF"]
                        if damageplayer > 0:
                            Orc["HP"] -= damageplayer
                        damageOrc = Orc["STR"] - player["DEF"]
                        if damageOrc > 0:
                            player["HP"] -= damageOrc
                        if Orc["HP"] <= 0:
                            print("Your win")
                        elif player["HP"] <= 0:
                            print("Your die")
                        else :
                            solanlap.append(_)
                        print(player)
                        print(Orc)
            elif option == "2":
                player["HP"] = 100
                print("Bạn đã được hồi phục HP")
                print("HP", player["HP"])
                print("Bạn gặp 1 con Orc")
                print("1. Chạy ra khỏi khu vực này")
                print("2. Nấp vào hang đá bên cạnh")
                print("3. ĐÁNH!!!")
                option = input("Lựa chọn của bạn?")
                if option == "1":
                    print("Do bạn chạy quá chậm nên đã bị Orc bắt đi")
                elif option == "2":
                    print("Con Orc không nhìn thấy bạn")
                    print("Tuy nhiên bạn quay lại nhìn vào trong hanh, bạn thấy một đàn sói")
                elif option == "3":
                    print("OPPONENT")
                    print(Orc)
                    solanlap = [0]
                    for _ in solanlap:
                        damageplayer = player["STR"] - Orc["DEF"]
                        if damageplayer > 0:
                            Orc["HP"] -= damageplayer
                        damageOrc = Orc["STR"] - player["DEF"]
                        if damageOrc > 0:
                            player["HP"] -= damageOrc
                        if Orc["HP"] <= 0:
                            print("Your win")
                        elif player["HP"] <= 0:
                            print("Your die")
                        else :
                            solanlap.append(_)
                        print("Player")
                        print("HP", player["HP"])
                        print("STR", player["STR"])
                        print("DEF", player["DEF"])
                        print("LUCK", player["LUCK"])
                        print("AGI", player["AGI"])
                        print("LVL", player["LVL"])
                        print("MiniOrc")
                        print("HP", Orc["HP"])
                        print("STR", Orc["STR"])
                        print("DEF", Orc["DEF"])
                        print("LUCK", Orc["LUCK"])
                        print("AGI", Orc["AGI"])
                        print("LVL", Orc["LVL"])

    else :
        print("Hãy nhập lại")