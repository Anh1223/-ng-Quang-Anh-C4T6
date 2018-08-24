def cautraloi_false() :
        print("What?")
        print("I don't can read")
        print("Please re-enter cmd")
        cmd = input("What command (fd, bd, lt, rt)")
        cmd = cmd.lower()
        cmd_list = cmd.split(" ")
        for c in cmd_list:
            if c == "fd":
                turtlelist.forward(100)
            if c == "bd":
                turtlelist.backward(100)
            if c == "lt":
                turtlelist.left(100)
            if c == "rt":
                turtlelist.right(100)
            else:
                print("What?")
                print("I don't can read")
                print("Please re-enter cmd")
                cautraloi_false()

from turtle import *
speed(0)
turtle_list = []
while True:
    for _ in range(9):
        turtle_list.append(Turtle())

    tp = int(input("Which one do you want to control?"))
    turtlelist = turtle_list[tp - 1]
    turtlelist.color(input("What color?"))
    cmd = input("What command (fd, bd, lt, rt)")
    cmd = cmd.lower()
    cmd_list = cmd.split(" ")
    for c in cmd_list:
        if c == "fd":
            turtlelist.forward(100)
        if c == "bd":
            turtlelist.backward(100)
        if c == "lt":
            turtlelist.left(100)
        if c == "rt":
            turtlelist.right(100)
        else:
           cautraloi_false()

mainloop()