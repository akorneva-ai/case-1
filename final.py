from turtle import *
import math
shape("turtle")
pensize(1)
pu()
def triangle_isosceles(x, y, a, b):
    """
    Function, drawing isosceles triangle.
    :param x: x coordinate in the left corner of the base
    :param y: y coordinate in the left corner of the base
    :param a: length of the triangle base
    :param b: length of the sides of the triangle
    :return: None
    """
    angle_base = math.degrees(math.acos(a / (2*b))) #угол при основании
    angle_top = 180 - 2 * angle_base #угол при вершине
    goto(x, y)
    color("red", "red")
    begin_fill()
    pd()
    fd(a)
    lt(180 - angle_base)
    fd(b)
    lt(180 - angle_top)
    fd(b)
    lt(180 - angle_base)
    end_fill()
    pu()
def rectangle(x, y, w, h):
    """
    Function, drawing rectangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param w: width of a rectangle
    :param h: height of a rectangle
    :return: None
    """
    goto(x,y)
    color("purple", "purple")
    begin_fill()
    pd()
    fd(w)
    rt(90)
    fd(h)
    rt(90)
    fd(w)
    rt(90)
    fd(h)
    rt(90)
    end_fill()
    pu()


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
def Circle(x, y, z):
    goto(x, y)
    down()
    begin_fill()
    circle(z)
    fillcolor('green')
    end_fill()
    up()
def paralelogram(x, y, z, w):
    goto(x, y)
    down()
    begin_fill()
    fillcolor('turquoise')
    lt(90)
    fd(z)
    lt(45)
    fd(w)
    lt(135)
    fd(z)
    lt(45)
    fd(w)
    lt(45)
    end_fill()
    up()
def triangle_pr(x, y, z):
    goto(x, y)
    down()
    begin_fill()
    fillcolor('crimson')
    fd(z * 3 ** 0.5)
    lt(150)
    fd(z*2)
    lt(120)
    fd(z*1)
    lt(90)
    end_fill()
    up()
def hvost(x, y, z):
    goto(x,y)
    down()
    begin_fill()
    fillcolor('grey')
    lt(120)
    fd(z)
    lt(100)
    fd(z*0.347)
    lt(100)
    fd(z)
    lt(40)
    end_fill()
    up()
done()
hideturtle()
