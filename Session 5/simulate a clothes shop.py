Ouritem = ["T-Shirt", "Sweater"]

while True:
    cauhoi = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    cauhoi = cauhoi.lower()
    if cauhoi == "r":
        print("Our items:", Ouritem)
    elif cauhoi == "c":
        Ouritem.append(input("Enter new item: "))
        print("Our items:", Ouritem)
    elif cauhoi == "u":
        Updateposition = int(input("Update position? "))
        Update = Updateposition - 1
        Ouritem.pop(Update)
        Ouritem.insert(Update, input("New item? "))
        print("Our items:", Ouritem)
    elif cauhoi == "d":
        Updateposition = int(input("Delete position? "))
        Update = Updateposition - 1
        Ouritem.pop(Update)
        print("Our items:", Ouritem)
    else:
        print("What?")
        print("I do not know what you are talking about")