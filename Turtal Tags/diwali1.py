#Small happy diwali


import turtle
import time
import random


c = turtle.Screen()
# c.setup(width=1.0, height=0.1)
c.bgcolor("#121212")
c.title("HAPPY DEWALI")
c.colormode(255)

t = turtle.Turtle()
t.speed(0)

def H():
    t.penup()
    t.setpos(-300, 200)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(180)
    t.fd(100)

def A():
    t.penup()
    t.setpos(-200, 200)
    t.pendown()
    t.left(90)
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(180)
    t.fd(50)
    t.right(60)
    t.fd(50)

def P():
    t.penup()
    t.setpos(-50, 200)
    t.pendown()
    t.left(150)
    t.fd(80)
    t.right(180)
    t.circle(25)

def Pp():
    t.penup()
    t.setpos(50, 200)
    t.pendown()
    t.left(180)
    t.fd(80)
    t.right(180)
    t.circle(25)

def Y():
    t.penup()
    t.setpos(150, 200)
    t.pendown()
    t.left(150)
    t.fd(110)
    t.right(180)
    t.fd(60)
    t.right(120)
    t.fd(60)
    t.right(180)
    t.fd(60)
    t.right(60)
    t.fd(50)
    t.left(120)

def D():
    t.penup()
    t.setpos(-350, 0)
    t.pendown()
    t.left(90)
    t.fd(100)
    t.right(90)
    t.circle(-50, 180, 30)
    t.right(180)

def I():
    t.penup()
    t.setpos(-250, 0)
    t.pendown()
    t.fd(50)
    t.left(180)
    t.fd(25)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(25)
    t.backward(50)

def W():
    t.penup()
    t.setpos(-150, 100)
    t.pendown()
    # t.color("blue")
    t.right(90)
    t.fd(100)
    t.left(135)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.left(135)
    t.fd(100)
    t.right(180)
    t.fd(100)

def A2():
    t.penup()
    t.setpos(-50, 0)
    t.pendown()
    t.left(90)
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(180)
    t.fd(50)
    t.right(60)
    t.fd(50)
    #t.color("white")

def L():
    t.penup()
    t.setpos(100, 0)
    t.pendown()
    t.left(150)
    t.fd(100)
    t.right(180)
    t.fd(100)
    t.left(90)
    t.fd(60)

def I2():
    t.penup()
    t.setpos(200, 0)
    t.pendown()
    t.fd(50)
    t.left(180)
    t.fd(25)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(25)
    t.backward(50) 


for i in range(5):
    radius = random.randint(80, 200)
    x_coord = random.randint(-400, 400)
    y_coord = random.randint(-300, 300)
    t.penup()
    t.setpos(x_coord,y_coord)
    t.pendown()
    B = random.randint(0, 255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    t.pencolor(R,G,B)
    for i in range(18):
        t.fd(radius)
        t.backward(2*radius)
        t.fd(radius)
        t.right(10)

t.setheading(0)
t.color("white")
t.pensize(10)

H()
A()
P()
Pp()
Y()
D()
I()
W()
A2()
L()
I2()
t.hideturtle()

time.sleep(4)

# Initials 
t.pencolor("black")
t.penup()
t.setpos(300, -200)
t.pendown()
t.setheading(0)
t.pensize(4)

#for graident background
for x in range(3):
    for i in range(0, 255):
        red = 255 - i
        green = 0
        blue = i
        c.bgcolor(red,green,blue)
        time.sleep(0.01)
    for i in range(0,255):
        red = i
        green = 0
        blue = 255 - i
        c.bgcolor(red,green,blue)
        time.sleep(0.01)


