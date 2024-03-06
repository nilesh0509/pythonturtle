import turtle
import math
import random
n=turtle.Turtle()
n.color("blue","red")
n.speed(0)
for i in range(4000):
    n.fd(10)
    n.lt(math.sin(i/10)*25)
    n.lt(20)

turtle.done()