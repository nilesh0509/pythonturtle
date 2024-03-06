#3D Building Using Python Turtle

from turtle import *


def r(x,y):
    rt(x)
    fd(y)

tracer(4)
fd(100)
bgcolor("black")
color("cyan")
width(3)
title("Building using python turtle")


for i in range(500):
    fd(i)
    r(90,i)
    r(90,i)
    r(270,i)
    r(90,i)
    circle(100,90)


#by VillainBytes


done()