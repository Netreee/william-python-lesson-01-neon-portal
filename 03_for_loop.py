import turtle

# Stage setup.
screen = turtle.Screen()
screen.setup(880, 820)
screen.bgcolor("#090E22")
screen.title("William | 3: Repeat the drawing rule")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)
t.pencolor("#32E4FF")

length = 8
growth = 2
steps = 120

for step in range(steps):
    t.forward(length)
    t.right(90)
    length = length + growth

screen.exitonclick()
