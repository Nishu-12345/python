from turtle import *
from colorsys import *
setpos(0, 80)
speed(0)
bgcolor('black')
pensize(2)
h = 0.02
for i in range(50):
    c = hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.004
    circle(20 -1, 90)
    lt(90)
    lt(90)
    circle(20 -1, 90)
    lt(18)
hideturtle()
done()

