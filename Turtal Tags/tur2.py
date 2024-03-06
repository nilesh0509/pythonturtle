import turtle as t

t.bgcolor('black')
t.tracer(100)
t.pensize(20)
c=['yellow', 'red', 'blue', 'green', 'purple']
t.rt(0.01)
for i in range(2600):
    t.color(c[i%3])
    t.down()
    t.circle(990-i,184)
    t.up()
    t.circle(990-i,184)
t.done()