from turtle import *

def right_triangle(x, y, a, b):
    penup()
    goto(x, y)
    pendown()
    color("black", "black")
    begin_fill()
    forward(a)
    left(90)
    forward(b)
    goto(x, y)
    end_fill()
    penup()

right_triangle(0, 0, 150, 200)
done()