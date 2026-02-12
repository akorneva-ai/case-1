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
triangle_isosceles(100,100,50,100)
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
done()