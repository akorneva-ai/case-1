from turtle import *
import math

from fontTools.misc.cython import returns

shape("turtle")
pensize(1)
pu()

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

def apple(x, y, z):
    Circle(x, y, z)

apple(0, 0, 50)
hideturtle()
done()