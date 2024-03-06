from turtle import *
title('The Lover')
bgcolor('black')
speed(0)
up()
goto(0,-300)
down()
begin_fill()
color('red','grey')
circle(300)
end_fill()
color('black')

#----Line fixing------#
up()
goto(-254,-160)
down()

#-----1st line-----#
fd(507)

#------ Turn left side-----#
lt(90)
fd(145)
rt(90)
fd(20)
lt(120)
fd(53)
lt(60)
fd(100)

#middel tringle
rt(45)
fd(120)
lt(90)
fd(100)
# lt(135)
# fd(210)
# lt(135)
# fd(30)

#------------Right Tringle side-----#
rt(135)
fd(100)

#-----Middle left tringle----#

rt(90)
fd(10)
lt(135)
fd(50)
lt(90)
fd(50)
lt(135)
fd(65)


#-------
bk(55)
rt(90)
fd(150)

#----------
lt(180)
fd(56)

#------
lt(90)
fd(125)
rt(110)
fd(55)
rt(70)
fd(106)

#-------
up()
goto(-175,51)
down()

#--------
rt(90)
fd(211)

#-------
# up()
# goto(-17,30)
# down()
up()
goto(17,71)
down()

#---------
rt(45)
fd(125)

#-------
# up()
# goto(-17,30)
# down()

#----------
lt(135)
fd(265)
lt(135)
fd(68)


#------
#-------
up()
goto(253,-15.5)
down()

#-----------
lt(45.5)
fd(60)


#-------
up()
goto(-60,-18)
down()

#-----------
lt(89.5)
fd(143)

#-------
up()
goto(187,-18)
down()

#-----
fd(143)

#-------
up()
goto(105.5,-160)
down()

#-----
lt(180)
fd(50)

circle(45,180)

fd(50)

#-------
up()
goto(-50,-25)
down()

#-----Middel left window-----
for i in range(4):
    fd(40)
    lt(90)

#-------
up()
goto(-34,-25)
down()

fd(40)
lt(90)
fd(5)
lt(90)
fd(40)

up()
goto(-10,-42)
down()

lt(90)
fd(40)
lt(90)
fd(5)
lt(90)
fd(40)

#-----Middle Right Window -----
#-------
up()
goto(137,-25)
down()

for i in range(4):
    fd(40)
    rt(90)

#-------
up()
goto(154,-25)
down()

#--------
rt(90)
fd(40)
lt(90)
fd(5)
lt(90)
fd(40)
lt(90)
fd(5)

#-------
up()
goto(177,-42)
down()

fd(40)
lt(90)
fd(5)
lt(90)
fd(40)
lt(90)
fd(5)

#----- LL Window------
#-------
up()
goto(-160,-10)
down()

for i in range(4):
    fd(50)
    rt(90)

#-------
up()
goto(-135.9,-10)
down()

fd(50)
rt(90)
fd(5)
rt(90)
fd(50)
rt(90)
fd(5)

#-------
up()
goto(-110,12)
down()

fd(50)
rt(90)
fd(4)
rt(90)
fd(50)
rt(90)
fd(5)

#-------
up()
goto(-130,-160)
down()

#------LL home-----
lt(180)
fd(80)
rt(90)
fd(70)
#tringle
lt(135)
fd(50)
lt(90.2)
fd(50)
#---gate---
up()
goto(-110,-160)
down()

rt(135)
fd(60)
rt(90)
fd(30)
rt(90)
fd(60)

#---RR home---
#-------
up()
goto(245,-160)
down()

rt(180)
fd(80)
lt(90)
fd(59)

#---gate---
up()
goto(230,-160)
down()

rt(90)
fd(60)
lt(90)
fd(30)
lt(90)
fd(60)

#---tringle---
up()
goto(187,-80)
down()

lt(135)
fd(45)
rt(96)
fd(43)

#---sun---
up()
goto(90,180)
down()

lt(45)
circle(40)

#---Circle inside the circle---
up()
goto(60,25)
down()

circle(30)

#---tree---
#-------
up()
goto(-245,-160)
down()

begin_fill()
fillcolor('#797979')
lt(120)
circle(-300,70)
rt(165)
# up()
# goto(-200,-160)
# down()

# lt(73)
circle(400,50)
rt(110)
fd(30)
end_fill()

#-----Leaf------
up()
goto(-185,175)
down()
lt(25)
fd(30)
rt(165)
fd(20)
lt(165)
fd(50)
rt(145)
circle(-120,40)
lt(145)
fd(30)
rt(145)
circle(-120,30)
lt(145)
fd(10)
rt(135)
# fd(50)
circle(-150,40)






# hideturtle()
done()