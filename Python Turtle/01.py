#  first turtle
import turtle
#  importing all from turtle.

pen = turtle.Turtle()
turtle.title("Heart Shape")
#  some functions with turtle.
pen.color('red')
pen.begin_fill()
pen.left(140)
pen.forward(180)
#pen.stamp()
pen.circle(-90, 200)
#pen.stamp()
pen.setheading(60)
#pen.stamp()
pen.circle(-90, 200)
#pen.stamp()
pen.forward(180)
pen.hideturtle()
pen.end_fill()

turtle.done()

#  it keep the animation window Open.
