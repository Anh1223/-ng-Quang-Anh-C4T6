colors = ['red', 'blue', 'brown', 'yellow', 'grey']
l = 3
g = 0
from turtle import *
speed(0)
hideturtle()
for c in colors:
    g = g + 180
    color(c)
    for i in range(l):
        forward(100)
        left(180 - (g / t))
    l = l + 1
mainloop()