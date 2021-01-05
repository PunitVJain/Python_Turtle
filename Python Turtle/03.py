# Third Turtle
import turtle
pen = turtle.Turtle()
turtle.title("Colorfull design")
color_list = ["red", "purple", "orange", "blue", "green"]
for iteam in range(500):
    pen.color(color_list[iteam % 5]) # color_list[iteam % 5] == > is to keep the iteam of the list in loop
    pen.pensize(iteam/10+1) #  pen size
    pen.forward(iteam)
    # pen.circle(iteam, steps= 3)
    pen.left(59)
    # pen.speed(10)


turtle.done()