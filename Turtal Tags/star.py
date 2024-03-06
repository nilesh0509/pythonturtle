import turtle
import time
import random
t=turtle.Turtle()
s=turtle.Screen()
s.title("spy.villain")
s.screensize(800,500,bg="black")
t.pencolor("blue")
t.write("villain" ,font=("Times New Roman", 20, "bold",))


t.speed(0)
def star():
    for i in range(5):
        t.pendown()
        t.forward(20)
        #time.sleep(1)
        t.right(144)
        
s.colormode(255)
while True:

    x=random.randint(-400,250)
    y=random.randint(-400,250)
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    t.pencolor(r,b,g)
    #t.write("villain")
    t.penup()
    t.goto(x,y)
    star()
turtle.done()