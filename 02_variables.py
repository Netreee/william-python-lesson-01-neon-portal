import turtle

# Stage setup.
screen = turtle.Screen()
screen.setup(880, 820)
screen.bgcolor("#090E22")
screen.title("William | 2: Make the path grow")

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)
t.pensize(4)
t.pencolor("#32E4FF")

length = 50
growth = 30

t.forward(length)
t.right(90)
length = length + growth

t.forward(length)
t.right(90)
length = length + growth

t.forward(length)
t.right(90)
length = length + growth

t.forward(length)
t.right(90)
length = length + growth

screen.exitonclick()
