import turtle

# Stage setup.
screen = turtle.Screen()
screen.setup(880, 820)
screen.bgcolor("#090E22")
screen.title("William | 4: Let the turtle choose a color")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

length = 8
growth = 2
steps = 200
color_boundary = 180

for step in range(steps):
    if length < color_boundary:
        t.pencolor("#32E4FF")
    else:
        t.pencolor("#FF53C8")

    t.forward(length)
    t.right(90)
    length = length + growth

screen.exitonclick()
