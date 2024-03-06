from turtle import *
import turtle as t
import time
t.colormode(255)


t.title('om namah shivay')
t.bgcolor('black')
t.color('grey')
t.speed(0)
t.screensize(1100, 1100)
t.pensize(20)
# upper
t.up()
t.goto(70,-50)
t.down()
t.lt(90)
t.fd(300)
t.lt(22)
t.circle(150,135)
t.lt(23)
t.fd(230)
t.rt(110)
t.fd(2)
t.circle(120,60)
t.circle(35,180)
t.up()
t.goto(70,-50)
t.down()
t.lt(170)
t.circle(-250,60)
t.up()
t.goto(70,20)
t.down()
t.rt(130)
t.circle(-180,70)
t.circle(60,65)
t.up()
t.goto(-250,-90)
t.down()
t.begin_fill()
t.lt(-45)
t.circle(360,68)
t.circle(-75,75)
t.circle(180,35)
t.lt(-88.8)
t.fd(30)
t.circle(-20,90)
t.circle(-110,40)
t.lt(95)
t.fd(150)
t.lt(120)
t.circle(-140,45)
t.lt(65)
t.circle(-40,180)
t.lt(-13.95)
t.fd(480)
t.circle(-40,150)
t.lt(45)
t.circle(-90,90)
t.lt(-75)
t.fd(10)
t.lt(-65)
t.circle(175,35)
t.lt(120)
t.fd(355)
t.lt(104)
t.circle(100,85)
t.circle(-282,70)
t.end_fill()

# eyes
t.pensize(10)
t.up()
t.goto(10,105)
t.down()
t.lt(85.5)
t.circle(-180,50)
t.circle(-35,150)
t.lt(170)
t.circle(-35,150)
t.circle(-180,40)
t.circle(-80,10)
t.circle(-35,150)
t.lt(170)
t.circle(-40,110)
t.circle(-120,10)
t.up()
t.goto(-79,180)
t.down()
t.color('white')
t.circle(10)
t.pensize(1)
t.up()
t.goto(-100,-190)
t.down()
t.lt(125.2)
t.color('blue')
t.write("OM NAMAH SHIVAY",font=("Times New Roman", 20, "bold",))
t.color('grey')

for x in range(3):
    for i in range(0, 255):
        red = 255 - i
        green = 0
        blue = i
        t.Screen().bgcolor(red,green,blue)
        t.speed(1)
for x in range(3):
    for i in range(0, 255):
        red = 255 - i
        green = 0
        blue = i
        t.Screen().bgcolor(red,green,blue)
        t.speed(1)





t.hideturtle()
t.done()