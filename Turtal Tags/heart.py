import math
from turtle import *
def heart(n):
    return 15*math.sin(n)**3
def heartn(n):
    return 12*math.cos(n)-5*\
        math.cos(2*n)-2*\
            math.cos(3*n)-\
                math.cos(4*n)
speed(0)
hideturtle()
bgcolor('black')
for i in range(600):
    goto(heart(i)*20,heartn(i)*20)
    for j in range(5):
        color('blue')
    goto(0,0)
done()