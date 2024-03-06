from turtle import *
colors=["deeppink","gold","cyan","orange"]
bgcolor('black')
r=[350,350]
turtles=[Turtle(),Turtle()]

for index,i in enumerate(turtles):
    i.speed(0)
    i.color('white')
    i.shape('circle')
    i.shapesize(0.3)
    i.width(3)
    i.pu()
    i.seth(90)
    i.fd(r[index])
    i.seth(180)
    i.pd()

turtles[0].pu()
tracer(30)
speed(0)
ht()

for i in colors:

done()
