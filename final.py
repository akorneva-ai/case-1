from turtle import *
import math
shape("turtle")
pensize(1)
pu()

def triangle_isosceles(x, y, a, b, contour, col):
    """
    Function, drawing isosceles triangle.
    :param x: x coordinate in the left corner of the base
    :param y: y coordinate in the left corner of the base
    :param a: length of the triangle base
    :param b: length of the sides of the triangle
    :param contour: contour of the triangle
    :param col: color of the triangle
    :return: None
    """
    angle_base = math.degrees(math.acos(a / (2*b))) #угол при основании
    angle_top = 180 - 2 * angle_base #угол при вершине
    goto(x, y)
    color(contour, col)
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

def rectangle(x, y, w, h, contour, col):
    """
    Function, drawing rectangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param w: width of a rectangle
    :param h: height of a rectangle
    :param contour: contour of the triangle
    :param col: color of the triangle
    :return: None
    """
    goto(x,y)
    color(contour, col)
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
def square(x, y, s, contour, col):
    """
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param s: sides of the square
    :param contour: contour of the triangle
    :param col: color of the triangle
    :return: None
    """
    goto(x, y)
    pendown()
    color(contour, col)
    begin_fill()
    for i in range(4):
        forward(s)
        left(90)
    end_fill()
    penup()

def right_angled_triangle(x, y, j, c, contour, col):
    """"
    Function, drawing right angle triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param j: sides of the triangle
    :param c: sides of the triangle
    :param contour: contour of the triangle
    :param col: color of the triangle
    :return: None
    """
    goto(x, y)
    pendown()
    color(contour, col)
    begin_fill()
    forward(j)  #первый катет
    left(90)
    forward(c)  #второй катет
    goto(x, y)  #вернуться к началу (гипотенуза)
    end_fill()
    penup()

def Circle(x, y, z, contour, col):
    """
    Function, drawing green circle.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param z: radius of circle
    :param contour: contour of the triangle
    :param col: color of the triangle
    :return: None
    """
    color(contour, col)
    goto(x, y)
    down()
    begin_fill()
    circle(z)
    end_fill()
    up()

def paralelogram(x, y, z, w, contour, col):
    """
    Function, drawing parallelogram.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param z: first side of parallelogram
    :param w: second side of parallelogram
    :param contour: contour of the triangle
    :param col: color of the triangle
    :return: None
    """
    goto(x, y)
    down()
    begin_fill()
    color(contour, col)
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
def equilateral_triangle(x, y, z, contour, col):
    """
    Function, drawing equilateral triangle.
    :param x: left bottom corner of the pink equilateral triangle
    :param y: left bottom corner of the pink equilateral triangle
    :param z: length of the pink equilateral triangle side
    :param contour: contour of the triangle
    :param col: color of the triangle
    :return: None
    """
    goto(x, y)
    color(contour, col)
    begin_fill()
    pd()
    for i in range(3):
        fd(z)
        lt(120)
    end_fill()
    pu()
def cat(x, y):
    #туловище кота
    rectangle(0, 0, 100, 50)
    #ноги кота
    square(x+30, y-50, -30)
    square(x+100, y-50, -30)
    #голова кота
    square(x+100, y-25, 50)
    #часть хвоста кота
    rectangle(x-50, y+15, 50, 25)
    #часть хвоста кота
    paralelogram(x-50, y-12, 25, 35)
    #конец хвоста

def apple(x, y, z):
    Circle(x, y, z)

#функция домика
def house(x, y):
    square(x, y,100)
    square(x+25, y+25, 50)
    lt(135)
    right_angled_triangle(x+125, y+100, 106, 106)
    lt(135)
    Circle(x+50, y+120, 15)
#house(100,100)

#функция рыбки
def fish(x, y):
    lt(45)
    right_angled_triangle(x, y, 106, 106)
    lt(90)
    right_angled_triangle(x, y+150, 106,106)
    lt(90)
    right_angled_triangle(x-150, y, 106, 106)
    rt(135)
    Circle(x+25, y+70, 10)

#fish(-200,100)
done()
hideturtle()