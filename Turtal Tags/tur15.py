from turtle import *
from time import sleep

bgcolor('black')
t=[Turtle(),Turtle()]
x=7
color=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
#t.title('spy.villain')
for index, i in enumerate(t):
    i.speed(0)
    i.color('white')
    i.shape('circle')
    i.shapesize(0.3)
    i.width(3)
    i.pu()
    i.seth(90)
    i.fd(350)
    i.seth(-180)
    i.pd()
t[0].pu()

delay(0)
speed(0)
#t.done()