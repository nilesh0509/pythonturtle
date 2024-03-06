import turtle as t 
import colorsys
t.bgcolor('black')
t.tracer(1000)
h = 0
t.pensize(2)
t.up()
t.goto(480,-400)
t.down()
t.lt(80)
t.fd(250)
for i in range(5000):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.01
    t.pencolor(c)
    #t.pensize(5)
    #t.up()
    #t.goto(-580,-500)
    #t.down()
    #t.lt(100)
    #t.fd(300)
    t.lt(i)
    t.fd(3)
    t.fd(5)
    t.write('YADUWANSHI',font=('kenia',100,'bold'))
t.done()