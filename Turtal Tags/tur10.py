from turtle import *
import colorsys
tracer(50)
bgcolor('black')
h=0.4
pensize(5)
for n in range(1000):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.0005
    forward(n*2)
    circle(n*2,-60)
    left(350)
done()