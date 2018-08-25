from turtle import *
speed(0)
turtle_list = []
for _ in range(9):
    turtle_list.append(Turtle())

def kiemcautraloi_turtlecandieukhienfalseortrue():
    if tp > 9:
        print("You can only choose one of the 9 turtles, ranked in order of 1 to 9")
        print("Please enter the serial number of the turtle to control")
        cautraloi_turtlecandieukhienfalse2()
    if tp < 1:
        print("You can only choose one of the 9 turtles, ranked in order of 1 to 9")
        print("Please enter the serial number of the turtle to control")
        cautraloi_turtlecandieukhienfalse2()

def cautraloi_turtlecandieukhienfalse2():
    tp = int(input("Which one do you want to control?"))
    if tp > 9:
        print("You can only choose one of the 9 turtles, ranked in order of 1 to 9")
        print("Please enter the serial number of the turtle to control")
        cautraloi_turtlecandieukhienfalse2()
    if tp < 1:
        print("You can only choose one of the 9 turtles, ranked in order of 1 to 9")
        print("Please enter the serial number of the turtle to control")
        cautraloi_turtlecandieukhienfalse2()
    else:
        turtlelist = turtle_list[tp - 1]
        colororcmd = input("Color or Shape or Color Shape")
        colororcmd = colororcmd.lower()
        colororcmd_list = colororcmd.split(" ")
        for _ in colororcmd_list:
            if _ == "color":
                turtlelist.color(input("What color?"))
            elif _ == "shape":
                turtlelist.shape(input("The shape to be changed"))
            else:
                print("What?")
                print("I don't can read")
                print("Please re-enter")
                color_shape(tp)

def color_shape(tp) :
    turtlelist = turtle_list[tp - 1]
    colororcmd = input("Color or Shape or Color Shape")
    colororcmd = colororcmd.lower()
    colororcmd_list = colororcmd.split(" ")
    for _ in colororcmd_list:
        if _ == "color":
            turtlelist.color(input("What color?"))
        elif _ == "shape":
            turtlelist.shape(input("The shape to be changed"))
        else:
            print("What?")
            print("I don't can read")
            print("Please re-enter")
            color_shape(tp)

while True:

    tp = int(input("Which one do you want to control?"))
    kiemcautraloi_turtlecandieukhienfalseortrue()
    if 9 > tp > 1 :
        turtlelist = turtle_list[tp - 1]
        colororcmd = input("Color or Shape or Color Shape")
        colororcmd = colororcmd.lower()
        colororcmd_list = colororcmd.split(" ")
        for _ in colororcmd_list:
            if _ == "color":
                turtlelist.color(input("What color?"))
            elif _ == "shape":
                turtlelist.shape(input("The shape to be changed"))
            else :
                print("What?")
                print("I don't can read")
                print("Please re-enter")
                color_shape(tp)

mainloop()
