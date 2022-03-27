from turtle import *

def drawCircle(t, centerpoint, radius):
    circumference = 2 * 3.14 * (radius/120)
    print("The circumference is " ,circumference)
    (x,y) = centerpoint
    t.up()
    t.setpos(x,y)
    t.down()
    t.circle(radius)


t = Turtle()
