import turtle
from turtle import *

wn = Screen()
wn.bgcolor('#393838')

t = turtle.Turtle()
t.pencolor('#daa520')
t.pensize(5)
wn.title('VilainBytes')

def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)

def heart():
    t.fillcolor('#cbc4a2')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

heart()
t.ht()

def write(message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('#daa520')
    t.pensize(5)
    Style=('Stencil Std', 18, 'bold','italic')
    t.write(message,font=Style)

write('I',(-68,88))
write('L',(-55,88))
write('O',(-42,88))
write('V',(-25,88))
write('E',(-10,88))
write('C',(11,88))
write('O',(28,88))
write('D',(47,88))
write('E',(65,88))

t.pencolor('gray')
t.up()
t.goto(50,-40)
t.down()
t.write('@Villain',font=('Stencil Std', 30, 'bold', 'italic'))

t.pencolor('#e2b13c')
t.up()
t.goto(198,-40)
t.down()
t.write('Bytes',font=('Stencil Std', 30, 'bold', 'italic'))

wn.mainloop()