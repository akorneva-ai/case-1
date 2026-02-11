from turtle import *

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

big_squareFill(0, 0, 100)

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

big_rectangleFill(-150, 0, 100, 50)
done()