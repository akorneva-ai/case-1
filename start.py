from turtle import *

#ф-ция квадрата
pensize(1)

def big_squareFill(x, y, a):
    penup()
    goto(x, y)
    pendown()
    color("orange", "orange")
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    penup()

#ф-ция прям-ного трегольника
def big_rectangleFill(x, y, b, c):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    color("red", "red")
    begin_fill()
    forward(b)
    left(90)
    forward(c)
    left(90)
    forward(b)
    left(90)
    forward(c)
    end_fill()
    setheading(0)
    penup()

