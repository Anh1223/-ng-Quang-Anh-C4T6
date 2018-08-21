colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import *
speed(0)
hideturtle()
for c in colors:
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
mainloop()