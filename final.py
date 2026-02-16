from turtle import *
import math
shape("turtle")
pensize(1)
pu()

def triangle_isosceles(x, y, a, b, col):
    """
    Function, drawing isosceles triangle.
    :param x: x coordinate in the left corner of the base
    :param y: y coordinate in the left corner of the base
    :param a: length of the triangle base
    :param b: length of the sides of the triangle
    :param col: color of the triangle
    :return: None
    """
    angle_base = math.degrees(math.acos(a / (2 * b))) #угол при основании
    angle_top = 180 - 2 * angle_base #угол при вершине
    goto(x, y)
    color("white", col)
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

def rectangle(x, y, w, h, col):
    """
    Function, drawing rectangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param w: width of a rectangle
    :param h: height of a rectangle
    :param col: color of the triangle
    :return: None
    """
    goto(x,y)
    color("white", col)
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

def square(x, y, s, col):
    """
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate yl
    :param s: sides of the square
    :param col: color of the triangle
    :return: None
    """
    goto(x, y)
    pendown()
    color("white", col)
    begin_fill()
    for i in range(4):
        forward(s)
        left(90)
    end_fill()
    penup()

def right_angled_triangle(x, y, j, c, col):
    """"
    Function, drawing right angle triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param j: sides of the triangle
    :param c: sides of the triangle
    :param col: color of the triangle
    :return: None
    """
    goto(x, y)
    pendown()
    color("white", col)
    begin_fill()
    forward(j)  #первый катет
    left(90)
    forward(c)  #второй катет
    goto(x, y)  #вернуться к началу (гипотенуза)
    end_fill()
    penup()

def Circle(x, y, z, col):
    """
    Function, drawing green circle.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param z: radius of circle
    :param col: color of the triangle
    :return: None
    """
    color("white", col)
    goto(x, y)
    down()
    begin_fill()
    circle(z)
    end_fill()
    up()

def paralelogram(x, y, z, w, col):
    """
    Function, drawing parallelogram.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param z: first side of parallelogram
    :param w: second side of parallelogram
    :param col: color of the triangle
    :return: None
    """
    goto(x, y)
    down()
    begin_fill()
    color("white", col)
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

def equilateral_triangle(x, y, z, col):
    """
    Function, drawing equilateral triangle.
    :param x: left bottom corner of the pink equilateral triangle
    :param y: left bottom corner of the pink equilateral triangle
    :param z: length of the pink equilateral triangle side
    :param col: color of the triangle
    :return: None
    """
    goto(x, y)
    color("white", col)
    begin_fill()
    pd()
    for i in range(3):
        fd(z)
        lt(120)
    end_fill()
    pu()

# ф-ция кощщки
def cat(x, y):
    rectangle(x, y, 100, 50, "orange")
    rectangle(x + 30, y, 40, 50, "black")
    square(x + 30, y - 50, -30, "orange")
    square(x + 100, y - 50, -30, "orange")
    square(x + 100, y - 25, 50, "orange")
    rectangle(x - 50, y + 15, 50, 25, "black")
    paralelogram(x - 50, y - 12.4, 25, 35, "orange")
    setheading(-30)
    equilateral_triangle(x - 96, y + 25, 25, "black")
    setheading(0)
    equilateral_triangle(x + 125, y + 25, 25, "black")
cat(200, 200)

#ф-ция яблока
def apple(x, y):
    Circle(0, 0, 50, "green")
    setheading(-60)
    equilateral_triangle(x - 12.5, y + 121.6, 25, "brown")
    setheading(0)
apple(0, 0)

#функция домика
def house(x, y):
    square(x, y,100,"pink")
    square(x + 25, y + 25, 50, "azure")
    lt(135)
    right_angled_triangle(x + 125, y + 100, 106, 106, "rosy brown")
    lt(135)
    Circle(x + 50, y + 120, 15, "light cyan")
house(100,-50)

#функция рыбки
def fish(x, y):
    lt(45)
    right_angled_triangle(x, y, 106, 106, "orange")
    lt(90)
    right_angled_triangle(x, y + 150, 106,106, "orange")
    lt(90)
    right_angled_triangle(x - 150, y, 106, 106, "orange")
    rt(135)
    Circle(x + 25, y + 70, 15, "indigo")
fish(-200,100)

#функция лисички
def lisiza(x,y, a, b, c, d, e, f, g, h, i, k):
    equilateral_triangle(x, y, a, b)
    rt(150)
    triangle_isosceles(x-(math.cos(1.25664) * 120) + 2, y+(math.sin(1.25664) * 120) - 2, c, d, e)
    rt(118.02+90)
    Circle(x +a / 2, y + ((a ** 2 - (a / 2) ** 2) **0.5), f, g)
    right_angled_triangle(x, y + ((a ** 2 - (a / 2) ** 2) ** 0.5) + 1.75 * (f), h, i, k)
    right_angled_triangle(x + a - 10, y + ((a ** 2 - (a / 2) ** 2) ** 0.5) + 1.75 * (f) - 25, h, i, k)
    lt(180)

#функция ракеты
def raketa(x, y, a, b, c, l, d,  e, f, g, h, i):
    rt(45)
    paralelogram(x, y, a, b, c)
    lt(45)
    square( x+ (a ** 2 - b ** 2) ** 0.5 - 16, y + b + 21, l, d)
    rt(90)
    right_angled_triangle(x + (a ** 2 - b ** 2) ** 0.5 + l - 16, y + l + 21 + l, e, f, g)
    lt(90)
    right_angled_triangle(x + (a ** 2 - b ** 2) ** 0.5 + l + f - 16, y + 21, e, f, g)
    rt(180)
    rt(90)
    right_angled_triangle(x + (a ** 2 - b ** 2) ** 0.5 - 25, y + b + l + e + 21, e, f, g)
    lt(90)
    right_angled_triangle(x + (a ** 2 - b ** 2) ** 0.5+f-25, y +21 + b + l, e, f, g)
    rt(180)
    equilateral_triangle(x + (a ** 2 - b ** 2) ** 0.5 - 24, y + b +l + e + 21, h, i)

#функция светофора
def svetofor(x, y):
    #большой прямоугольник
    rectangle(x, y, 100, 200, "gray")
    Circle(x + 50, y - 65, 30, "red")  #верхний красный
    Circle(x + 50, y - 130, 30, "yellow")  #средний желтый
    Circle(x + 50, y - 195, 30, "green")  #нижний зеленый
    #нижний прямоугольник
    rectangle(x + 30, y - 200, 40, 60, "gray")
svetofor(0, -80)

#функция чела
def chel(x,y):
    #голова
    square(x,y, 50, "black")
    #туловище
    equilateral_triangle(x - 15, y - 40 * math.sqrt(3), 80, "yellow")
    # руки
    equilateral_triangle(x - 15,y - 20 * math.sqrt(3), 25, "black")
    equilateral_triangle(x + 45, y - 20 * math.sqrt(3), 20, "black")
    # ноги
    square(x, y - 40 * math.sqrt(3) - 15, 15, "black")
    square(x + 30, y - 40 * math.sqrt(3) - 15, 15, "black")
chel(-200, -200)

hideturtle()
done()
