import turtle
import time
import turtle as t
t.title("Ravan")
t.speed(0)
t.hideturtle()
t.bgcolor("#C2DFFF")

t.colormode(255)


t1=turtle.Turtle()
t1.hideturtle()
def pos1(x,y):
    t1.penup()
    t1.goto(x,y) 
    t1.pendown()

def pos(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
pos(-80,130)
t.right(30)
for i in range(3,13):
    t.pensize(i)
    t.left(3)
    t.forward(7)
for i in range(13,3,-1):
    t.pensize(i)
    t.left(3)
    t.forward(7)
pos(-70,115)
t.right(60)
for i in range(3,13):
    t.pensize(i)
    t.left(3)
    t.forward(6)
for i in range(13,3,-1):
    t.pensize(i)
    t.left(3)
    t.forward(6)
pos(-60,100)
t.right(60)
for i in range(3,13):
    t.pensize(i)
    t.left(3)
    t.forward(5)
for i in range(13,3,-1):
    t.pensize(i)
    t.left(3)
    t.forward(5)
t.color("black","dark orange")
pos(-5,90)
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")
pos(0,70)
t.begin_fill()
t.right(80)
t.forward(20)
t.left(90)
t.forward(60)
t.left(7)
t.forward(40)
t.right(110)
t.forward(50)
t.right(155)
t.forward(27)
t.left(75)
t.forward(100)
t.right(115)
t.forward(30)
t.end_fill()

t.color("black")
pos(-30,70)
t.begin_fill()
t.right(50)
t.back(20)
t.right(90)
t.back(60)
t.right(7)
t.back(40)
t.left(110)
t.back(50)
t.left(155)
t.back(27)
t.right(75)
t.back(100)
t.left(115)
t.back(30)
t.end_fill()

pos(-60,30)
t.right(45)
t.pensize(10)
for i in range(5):
    t.left(2)
    t.forward(2)
t.pensize(9)
for i in range(5):
    t.left(2)
    t.forward(2)
t.pensize(8)
for i in range(20):
    t.right(7)
    t.forward(4)
t.left(30)
for i in range(10):
    t.left(2)
    t.forward(2)
t.right(170)
for i in range(10):
    t.left(2)
    t.forward(2)
t.left(15)
for i in range(10):
    t.right(3)
    t.forward(5)
t.pensize(9)
for i in range(5):
    t.left(2)
    t.forward(2)
t.pensize(10)
for i in range(5):
    t.left(2)
    t.forward(2)

t.pensize(10)
pos(-90,40)
t.right(65)
for i in range(30):
    t.right(7)
    t.forward(1)

pos(30,30)
t.left(65)
t.pensize(10)
for i in range(5):
    t.right(2)
    t.back(2)
t.pensize(9)
for i in range(5):
    t.right(2)
    t.back(2)
t.pensize(8)
for i in range(20):
    t.left(7)
    t.back(4)
t.right(30)
for i in range(10):
    t.right(2)
    t.back(2)
t.left(170)
for i in range(10):
    t.right(2)
    t.back(2)
t.right(15)
for i in range(10):
    t.left(3)
    t.back(5)
t.pensize(9)
for i in range(5):
    t.right(2)
    t.back(2)
t.pensize(10)
for i in range(5):
    t.right(2)
    t.back(2)
t.pensize(10)
pos(60,40)
t.right(80)
for i in range(30):
    t.left(7)
    t.forward(1)
t.pensize(6)
pos(10,10)
t.right(35)
t.back(100)
pos(20,-95)
t.left(110)
t.back(15)
t.right(90)
t.back(15)
t.right(90)
t.back(45)
t.right(30)
t.back(10)

pos(-30,10)
t.left(80)
t.back(100)
pos(-40,-95)
t.right(110)
t.back(15)
t.left(90)
t.back(15)
t.left(90)
t.back(45)
t.left(30)
t.back(10)

pos(-15,150)
t.right(60)
for i in range(10):
    t.left(5)
    t.forward(10)
t.left(5)
for i in range(9):
    t.left(1)
    t.forward(5)
t.left(77)
t.forward(270)
t.left(75)
t.forward(75)
pos(-150,-80)
t.right(70)
t.forward(50)
t.left(75)
for i in range(13):
    t.right(5)
    t.forward(13)
t.left(85)
t.forward(50)
pos(-15,150)
t.left(60)
for i in range(10):
    t.right(5)
    t.forward(10)
t.right(5)
for i in range(9):
    t.right(1)
    t.forward(5)

t.right(77)
t.forward(270)
t.right(75)
t.forward(75)
pos(130,-78)
t.left(70)
t.forward(50)
t.right(75)
for i in range(13):
    t.left(5)
    t.forward(13)
t.right(85)
t.forward(50)


pos(-15,150)
t.begin_fill()
t.right(60)
for i in range(10):
    t.left(5)
    t.forward(10)
t.left(5)
for i in range(9):
    t.left(1)
    t.forward(5)
t.right(5)
t.forward(60)
t.right(120)
for i in range(11):
    t.right(5)
    t.forward(20)
t.end_fill()
pos(-15,150)
t.begin_fill()
t.left(58)
for i in range(10):
    t.right(5)
    t.forward(10)
t.right(5)
for i in range(9):
    t.right(1)
    t.forward(5)
t.left(5)
t.forward(60)
t.left(120)
for i in range(11):
    t.left(5)
    t.forward(20)
t.end_fill()
pos(-140,200)
t.begin_fill()
pos(-200,200)
t.left(82)
t.forward(270)
for i in range(10):
    t.right(6)
    t.forward(15)
t.right(25)
for i in range(10):
    t.left(6)
    t.back(15)
t.left(27)
for i in range(10):
    t.right(5)
    t.forward(15)
t.right(25)
for i in range(15):
    t.left(5)
    t.back(15)
t.end_fill()


pos(110,210)
t.begin_fill()
pos(170,210)
t.left(20)
t.forward(270)
for i in range(10):
    t.left(6)
    t.forward(15)
t.left(25)
for i in range(10):
    t.right(6)
    t.back(15)
t.right(27)
for i in range(10):
    t.left(5)
    t.forward(15)
t.left(25)
for i in range(15):
    t.right(5)
    t.back(15)
t.end_fill()


#for mucch
pos1(-10,-125)
t1.pensize(7)
t1.begin_fill()
t1.forward(10)
t1.left(30)
t1.forward(45)
t1.left(90)

for i in range(10):
    t1.left(2)
    t1.back(10)
t1.left(5)
for i in range(10):
    t1.left(7)
    t1.back(3)
t1.left(55)
for i in range(10):
    t1.right(7)
    t1.forward(3)
t1.right(20)
for i in range(12):
    t1.right(3)
    t1.forward(12)
t1.end_fill()

t1.right(145)
pos1(-10,-125)
t1.pensize(7)
t1.begin_fill()
t1.back(10)
t1.right(30)
t1.back(45)
t1.right(90)
for i in range(10):
    t1.right(2)
    t1.fd(10)
t1.right(5)
for i in range(10):
    t1.right(7)
    t1.fd(3)
t1.right(55)
for i in range(10):
    t1.left(7)
    t1.back(3)
t1.left(20)
for i in range(12):
    t1.left(3)
    t1.back(12)
t1.end_fill()

t.up()
t.goto(0,-320)
t.down()
t.color("#C2DFFF")
t.write("@villainbytes 😈",font=('verdana',30,'italic'))

#for graident background
for x in range(3):
    for i in range(0, 255):
        red = 255 - i
        green = 0
        blue = i
        t.Screen().bgcolor(blue,green,red)
        time.sleep(0.001)
for x in range(3):
    for i in range(0, 255):
        red = 255 - i
        green = 0
        blue = i
        t.Screen().bgcolor(red,green,blue)
        time.sleep(0.001)


t.exitonclick()
