from turtle import *
bgcolor('white')
speed(100)
pencolor('green')
def draw(size):
    size += 10 
    right(15)
    right(180)
    right(15)
    for i in range(4):
        forward(size)
        right(90)
x = 200
for i in range(8):
    for j in range(6):
        print("I LOVE MY OWN :")
        draw(x)
        # print("I LOVE MY OWN : ")
hideturtle()
done()                
