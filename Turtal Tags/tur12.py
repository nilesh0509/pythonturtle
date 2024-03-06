import turtle as t
import colorsys as c
t.setup(800,800)
t.speed(0)
t.tracer(100)
t.width(2)
t.bgcolor("black")
for j in range(70):
    for i in range(80):
        t.color(c.hsv_to_rgb(i/25,j/25,1))
        t.right(90)
        t.circle(200-j*4,90)
        t.left(90)
        t.circle(200-j*4,90)
        t.right(180)
        t.circle(50,24)
#t.hideturtle()
t.down()
