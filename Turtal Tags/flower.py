import turtle
t=turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')
color=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtle.title('spy.villain')
for i in range(200):
    t.color(color[i%7])
    t.pensize(i/7)
    t.forward(i)
    t.left(45)

turtle.hideturtle()
turtle.done()