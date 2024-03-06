#3D_Cube Using Python Turtle

import time
import turtle

a=int(input('Enter length of cube: '))
b=int(input('angle of cube: '))

t=turtle.Turtle()
s=turtle.Screen()
s.title('VillainBytes') #it is for title of turtle
s.screensize(800,500,bg="black") #it is for size of screen 
t.pencolor('grey')
t.pensize(3)
def cube(a):
    for i in range(4):
        t.forward(a)
        t.left(90)
def square(a,b):
    cube(a)
    t.left(b)
    t.fd(a)
    #time.sleep(2)
    t.right(b)
    #time.sleep(2)
    cube(a)
    t.left(90)
    t.forward(a)
    t.left(90+b)
    t.fd(a)
    t.rt(b+180)
    t.fd(a)
    t.lt(b)
    t.fd(a)
    t.rt(b+90)
    t.fd(a)
    t.rt(90-b)
    t.fd(a)
square(a,b)

        
# cube()
# t.left(30)
# t.fd(100)
# #time.sleep(2)
# t.right(30)
# #time.sleep(2)
# cube()
# t.left(90)
# t.forward(100)
# t.left(90+30)
# t.fd(100)
# t.rt(30+180)
# t.fd(100)
# t.lt(30)
# t.fd(100)
# t.rt(30+90)
# t.fd(100)
# t.rt(60)
# t.fd(100)
turtle.done()