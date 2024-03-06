#tutorial desing by spycodern.

import turtle as t
import colorsys
t.Screen().bgcolor('black')
tu=t.Turtle()
tu.speed(0)
h=0.8
tu.pensize(1)
def deg(a,n):
    tu.circle(n*1.2,90)
    tu.left(a)
    tu.circle(n*1.2,90)
for i in range(95):
    c=colorsys.hsv_to_rgb(h,0.9,1)
    tu.pencolor(c)
    deg(135,i)
    deg(135,i)
    deg(90,i)
    deg(135,i)
    deg(135,i)
    h+=0.005
t.done()