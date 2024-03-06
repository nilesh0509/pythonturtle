import turtle
import time



t=turtle.Turtle()
s=turtle.Screen()
s.title('villain')
s.bgcolor('black')
t.pencolor('purple')

t.speed(0)
a=0
while(True):
    for i in range(4):
        t.fd(100)
        t.rt(90)
    
    t.rt(5)
    a+=1
    if a>=360/5:
        break



t.hideturtle()
turtle.done()