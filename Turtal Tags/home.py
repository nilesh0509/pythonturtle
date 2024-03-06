from turtle import *
title("Villain's Home")
screensize(800,800)
speed(0)
up()
goto(150,-200)
down()
bgcolor('#5AC8F0')

begin_fill()
fd(200)#ract
lt(90)
fd(300)
lt(90)
fd(400)
lt(90)
fd(300)
lt(90)
fd(200)
fillcolor("#A2AD9C")
end_fill()

begin_fill()
fd(50)#chokhat
lt(90)
fd(10)
lt(90)
fd(100)
lt(90)
fd(10)
lt(90)
fd(100)
fillcolor("#DAEE01")
end_fill()

lt(90)
fd(10)
lt(90)
fd(10)
rt(90)
begin_fill()
fd(200)
lt(90)
fd(80)
lt(90)
fd(200)
fillcolor("#7CFC00")
end_fill()


up()
goto(100,-100)
down()

begin_fill()
fillcolor('yellow')
lt(180)
fd(50)
lt(90)
fd(10)
lt(90)
fd(50)
lt(90)
fd(10)
end_fill()

lt(90)
fd(50)
lt(90)
fd(5)

begin_fill()
fillcolor('orange')
circle(-6)
end_fill()

up()
goto(70,-100)
down()

begin_fill()
fillcolor("#551606")
fd(100)
rt(90)
fd(5)
rt(90)
fd(100)
rt(90)
fd(5)
end_fill()

bk(5)
rt(90)
fd(10)
rt(90)

begin_fill()
for i in range(4):#big square
    fillcolor('#5865F2')
    fd(80)
    lt(90)
end_fill()

for i in range(4):
    fd(40)
    lt(90)

fd(40)
for i in range(4):
    fd(40)
    lt(90)

fd(40)
lt(90)
fd(40)

for i in range(4):
    fd(40)
    lt(90)

up()
goto(220,-100)
down()

begin_fill()
fillcolor("#551606")
rt(180)
fd(100)
rt(90)
fd(5)
rt(90)
fd(100)
rt(90)
fd(5)
end_fill()

rt(90)
fd(10)
lt(90)

begin_fill()
for i in range(4):#big square
    fillcolor('#5865F2')
    fd(80)
    rt(90)
end_fill()
    
for i in range(4):
	fd(40)
	rt(90)
	
fd(40)

for i in range(4):
	fd(40)
	rt(90)
	
fd(40)
rt(90)
fd(40)

for i in range(4):
	fd(40)
	rt(90)


up()
goto(350,100)
down()

begin_fill()
fillcolor("#551606")
fd(50)#first tringle
lt(135)
fd(350)
lt(90)
fd(350)
lt(135)
fd(45)
end_fill()

up()
lt(90)
fd(15)
rt(90)
down()

begin_fill()
fillcolor('#915F6D')
fd(400)#second tringle
lt(135)
fd(280)
lt(89.5)
fd(284)
end_fill()

up()
goto(-25,170)
rt(135)
down()

begin_fill()
fillcolor("#551606")
fd(100)#tower
lt(90)
fd(50)
rt(90)
fd(20)
rt(90)
fd(120)
rt(90)
fd(20)
rt(90)
fd(50)
lt(90)
fd(80)
end_fill()



up()
goto(-300,340)
down()

begin_fill()
fillcolor('yellow')
circle(60)#sun
end_fill()

up()
goto(185,-85)
down()
begin_fill()
fillcolor('#551606')
circle(-10)#lock
end_fill()

up()
goto(150,130)
# lt(180)
# fd(350)
lt(90)
down()

begin_fill()
fillcolor('#3E9285')
left(135)
forward(80)
circle(-40,180)
# # lt(120)
setheading(45)
circle(-40,180)
forward(80)
end_fill()
# color('#8366E5')

hideturtle()
done()