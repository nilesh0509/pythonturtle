#by spy villain uff spycodern😎😇

import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(10)
h = 0.1
for i in range(500):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    t.color(c)
    t.up()
    t.goto(-160,10)
    t.down()
    t.lt(18)
    t.fd(10)
    t.write('SPY villain',font=('verdana',50,'italic'))
    t.lt(2)
    #t.write('VILLAIN',font=('verdana',60,'italic'))
t.done()