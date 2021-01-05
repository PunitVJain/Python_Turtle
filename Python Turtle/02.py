# second turtle
#  turtle moduel to create the star.

import turtle
n = 100 
pen = turtle.Turtle()

for i in range(n):
    pen.forward(i * 5)
    #in clockwise
    pen.right(160)

turtle.done()

