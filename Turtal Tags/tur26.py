from turtle import *

def N():
    fd(25)
    rt(90)
    fd(10)
    rt(90)
    fd(50)
    rt(135)
    fd(70)
    lt(45)
    fd(10)
    lt(90)
    fd(70)
    lt(90)
    fd(10)
    lt(90)
    fd(30)
    
    up()
    goto(-306,35)
    down()

    fd(35)
    rt(135)
    fd(80)

    up()
    goto(-370,-25)
    down()

    rt(45)
    fd(75)
    rt(135)
    fd(85)

def I():

    up()
    goto(-270,-12.5)
    down()

    rt(45)
    fd(12.5)
    rt(90)
    fd(10)
    rt(90)
    fd(70)
    rt(90)
    fd(5)
    rt(90)
    fd(65)







if __name__ == '__main__':
    bgcolor('black')
    color('white')
    up()
    goto(-350,0)
    rt(90)
    down()
    N()
    I()
    # hideturtle()
done()


