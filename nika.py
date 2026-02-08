from turtle import *
shape("turtle")
pensize(1)
pu()
def triangle_small(x, y):
    color("blue", "blue")
    begin_fill()
    goto(x, y)
    pd()
    fd(50)
    rt(120)
    fd(50)
    rt(120)
    fd(50)
    rt(120)
    pu()
    end_fill()

done()