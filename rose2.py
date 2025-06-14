import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle object
rose = turtle.Turtle()
rose.speed(0)
rose.color("red", "pink")  # pen color, fill color
rose.pensize(2)

# Draw the rose using polar coordinates
def draw_rose(k, n_petals):
    rose.begin_fill()
    for theta in range(60 * 5):  # draw more loops for a fuller rose
        t = math.radians(theta)
        r = 200 * math.sin(k * t)
        x = r * math.cos(t)
        y = r * math.sin(t)
        rose.goto(x, y)
    rose.end_fill()

# Move to starting position
rose.penup()
rose.goto(0, 0)
rose.pendown()


draw_rose(k=7, n_petals=7)

# Hide turtle and keep window open
rose.hideturtle()
turtle.done()
