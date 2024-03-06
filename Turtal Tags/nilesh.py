import turtle as t

s=t.Screen()
s.screensize(2814,1324)
t.bgcolor('black')
t.pencolor('blue')
t.title('spy.villain')
t.pensize(5)
t.speed(0)

#ni
t.left(90)
t.fd(100)
t.fd(-30)
t.left(30)
t.circle(30,200)

t.up()
t.goto(0,100)
t.down()

t.left(130)
t.fd(30)
t.lt(85)
t.fd(50)
t.circle(-100,30)
t.circle(-50,90)
t.circle(-40,90)

t.up()
t.goto(50,0)
t.down()

t.lt(125)
t.fd(130)
t.lt(30)
t.circle(270,31.5)

#line
t.up()
t.goto(-100,100)
t.down()
t.rt(151.5)
t.fd(280)


#e
t.up()
t.goto(100,100)
t.down()
t.rt(120)
t.fd(20)
t.circle(60,90)
t.begin_fill()
t.color('blue')
t.circle(5)
t.end_fill()

#l
t.up()
t.goto(150,0)
t.down()
t.lt(120)
t.fd(100)
t.fd(-30)
t.circle(10,180)
t.rt(150)
t.fd(5)
t.circle(10,220)
t.fd(15)
t.circle(2)


#sh
t.up()
t.goto(180,100)
t.down()
t.begin_fill()
#t.color('red')
t.lt(-25)
t.fd(20)
t.circle(-10,180)
t.lt(90)
t.circle(-10,210)
t.end_fill()
t.fd(35)
t.rt(105)
t.fd(100)
t.fd(-103)
t.lt(90)
t.fd(20)

t.up()
t.goto(-200,-100)
t.down()
t.color('red')
t.pensize(10)
t.write("!!💞🌹✨..nilesh12105..💞🌹✨!!",align="left",font=("Times New Roman", 30,'bold'))

t.hideturtle()
t.done()