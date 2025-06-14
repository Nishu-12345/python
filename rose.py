import turtle
def draw_rose(size, red):
    turtle.fillcolor(red)
    turtle.begin_fill()
    for  _ in range(360):
    
        turtle.forward(size)
        turtle.left(170)
        turtle.left(89)
        turtle.end_fill()
draw_rose(200, 'red')
turtle.penupz()
turtle.goto(0, -120)
turtle.write("Forever entwined...", align="center", 
             font=("Arial", 16, "bold"))
turtle.goto(0, -150)
turtle.write("You're my code, my passward, my cute friend...", align="center",
             font=("Arial", 14))
turtle.goto(0, -180)
turtle.write("- Your loving friend...", align="center", font=("Arial", 12))