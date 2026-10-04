import turtle

# Stage setup.
screen = turtle.Screen()
screen.setup(880, 820)
screen.bgcolor("#090E22")
screen.title("William | 1: Give the turtle directions")

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)
t.pensize(4)
t.pencolor("#32E4FF")

# Draw in this order.
t.forward(60)
t.right(90)
t.forward(60)

screen.exitonclick()
