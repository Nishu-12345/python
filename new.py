from turtle import*
import colorsys
speed(1000)
bgcolor("black")
h = 0
for i in range(160):
  for j in range(18):
      c = colorsys.hsv_to_rgb(h,1,1)
      color(c)
      h+= 0.007
      rt(90)
      circle(150 - j * 6, 90)
      lt(90)
      circle(150 - j * 6, 90)
      rt(180)
  circle(40, 54)
done()