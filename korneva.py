from turtle import *

pensize(1)

def big_squareFill(x, y):
    penup()
    goto(x, y)
    pendown()
    color("orange", "orange")
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    penup()

big_squareFill(0, 0)

def big_rectangleFill(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    color("red", "red")
    begin_fill()
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    end_fill()
    setheading(0)
    penup()

big_rectangleFill(-150, 0)
done()