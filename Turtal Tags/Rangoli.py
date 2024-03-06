import colorsys
import time
import turtle as t

t.bgcolor('black')
t.tracer(10)
t.ht()
h=0
for i in range(900):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.008
    t.pencolor(c)
    t.fd(i)
    t.lt(10)
    t.rt(50)
    t.circle(10)
    time.sleep(0.0000000000000000000000000001)
t.done()

#created by spycodern😇😇😇😇