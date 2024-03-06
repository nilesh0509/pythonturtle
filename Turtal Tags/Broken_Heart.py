from turtle import *
import turtle as t
import time

t.colormode(255)

color('red')
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()

penup()
goto(0,155)
pendown()
pencolor('black')
width(4)
fd(10)
right(70)
fd(20)
left(60)
fd(30)
right(70)
fd(30)
left(70)
fd(50)
right(55)
fd(50)
hideturtle()


#for graident background
for x in range(3):
    for i in range(0, 255):
        red = 255 - i
        green = 0
        blue = i
        t.Screen().bgcolor(red,green,blue)
        time.sleep(0.001)
for x in range(3):
    for i in range(0, 255):
        red = 255 - i
        green = 0
        blue = i
        t.Screen().bgcolor(red,green,blue)
        time.sleep(0.001)

#created by spycodern😇😇😇😇
