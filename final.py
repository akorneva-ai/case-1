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
    color("white", "red")
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
    color("white", "purple")
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

def square(x, y, s):
    """
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param s: sides of the square
    :return: None
    """
    goto(x, y)
    pendown()
    color("white", "orange")
    begin_fill()
    for i in range(4):
        forward(s)
        left(90)
    end_fill()
    penup()

def right_angled_triangle(x, y, j, c):
    """"
    Function, drawing right angle triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param j: sides of the triangle
    :param c: sides of the triangle
    :return: None
    """
    goto(x, y)
    pendown()
    color("white", "black")
    begin_fill()
    forward(j)  #первый катет
    left(90)
    forward(c)  #второй катет
    goto(x, y)  #вернуться к началу (гипотенуза)
    end_fill()
    penup()

def Circle(x, y, z):
    '''
    Function, drawing green circle.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param z: radius of circle
    :return: None
    '''
    color('white','green')
    goto(x, y)
    down()
    begin_fill()
    circle(z)
    end_fill()
    up()

def paralelogram(x, y, z, w):
    '''
    Function, drawing turquoise parallelogram.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param z: first side of parallelogram
    :param w: second side of parallelogram
    :return: None
    '''
    goto(x, y)
    down()
    begin_fill()
    color('white', 'turquoise')
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

done()
hideturtle()