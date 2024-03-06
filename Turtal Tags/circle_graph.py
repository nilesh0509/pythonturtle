import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
turtle.bgcolor("black")  
turtle.pensize(5)  
turtle.speed(0)  
  
while (True):  
    for i in range(2):  
        #for colors in ["#40E0D0", "red", "blue", "magenta", "green", "yellow", "white","gray","salmon"]:  
        for colors in ["#00FFFF"]:  
            turtle.color(colors)  
            turtle.circle(200)  
            turtle.left(5)  
  
  
turtle.hideturtle()  
turtle.mainloop()  