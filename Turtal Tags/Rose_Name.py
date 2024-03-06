from turtle import *
import turtle as tur
import time


tur.title("@spy.villain")
tur.write("🌹🌹Villain🌹🌹.!!",align="right",font=("Times New Roman", 25, "bold"))

tur.colormode(255)

# Set initial position
tur.penup ()
tur.left (90)
tur.fd (200)
tur.pendown ()
tur.right (90)

# flower base
tur.fillcolor ("red")
tur.begin_fill ()
tur.circle (10,180)
tur.circle (25,110)
tur.left (50)
tur.circle (60,45)
tur.circle (20,170)
tur.right (24)
tur.fd (30)
tur.left (10)
tur.circle (30,110)
tur.fd (20)
tur.left (40)
tur.circle (90,70)
tur.circle (30,150)
tur.right (30)
tur.fd (15)
tur.circle (80,90)
tur.left (15)
tur.fd (45)
tur.right (165)
tur.fd (20)
tur.left (155)
tur.circle (150,80)
tur.left (50)
tur.circle (150,90)
tur.end_fill ()

# Petal 1
tur.left (150)
tur.circle (-90,70)
tur.left (20)
tur.circle (75,105)
tur.setheading (60)
tur.circle (80,98)
tur.circle (-90,40)

# Petal 2
tur.left (180)
tur.circle (90,40)
tur.circle (-80,98)
tur.setheading (-83)

# Leaves 1
tur.fd (30)
tur.left (90)
tur.fd (25)
tur.left (45)
tur.fillcolor ("green")
tur.begin_fill ()
tur.circle (-80,90)
tur.right (90)
tur.circle (-80,90)
tur.end_fill ()
tur.right (135)
tur.fd (60)
tur.left (180)
tur.fd (85)
tur.left (90)
tur.fd (80)

# Leaves 2
tur.right (90)
tur.right (45)
tur.fillcolor ("green")
tur.begin_fill ()
tur.circle (80,90)
tur.left (90)
tur.circle (80,90)
tur.end_fill ()
tur.left (135)
tur.fd (60)
tur.left (180)
tur.fd (60)
tur.right (90)
tur.circle (200,60)

tur.write("🌹🌹I Love You..!!💞💞🌹🌹",align="right",font=("Times New Roman", 20, "bold",))
tur.color("red")

#for graident background
for x in range(3):
    for i in range(0, 255):
        red = 255 - i
        green = 0
        blue = i
        tur.Screen().bgcolor(red,green,blue)
        time.sleep(0.001)
for x in range(3):
    for i in range(0, 255):
        red = 255 - i
        green = 0
        blue = i
        tur.Screen().bgcolor(red,green,blue)
        time.sleep(0.001)


    

tur.done()