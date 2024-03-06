#colorfull flower


import colorsys
import turtle as t

t.bgcolor('black')
t.tracer(100)
t.width(7)
h = 0
n = 87
for i in range(3000):
    c = colorsys.hsv_to_rgb(h,1,.9)
    h += 1/n
    t.setposition(0,100)
    t.pencolor(c)
    t.left(50)
    t.circle(10)
    t.backward(42)
    t.rt(56)
    t.fd(i)
    t.bk(575)
t.done()

#created by spycodern😇😇😇😇