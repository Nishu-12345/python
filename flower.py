from turtle import *
import colorsys
speed(1)
bgcolor("black")
h = 0
for i in range(16):
  for j in range(18):
     
      h += 0.005
      c = colorsys.hsv_to_rgb(h, 3, 3)
      rt(98)
      circle(150 - j * 6, 90)
      lt(90)
      circle(150 - j * 6, 90)
      rt(180)
circle(40, 24)
done()