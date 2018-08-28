player = {              #ID: 0    (khi bị tấn công để random)
    "NAME": NAME,
    "HP": 400,
    "STR": 7,
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
    "HP": 100000,
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