import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up turtle
t = turtle.Turtle()
t.pensize(5)
t.color("blue")

# --- Draw the letter B ---
t.penup()
t.goto(-100, 0)
t.setheading(90)
t.pendown()


t.forward(100)


t.right(90)
t.circle(-20, 180)


t.left(180)
t.circle(-20, 180)

# --- Move to draw the letter E ---
t.penup()
t.goto(50, 0)
t.setheading(90)
t.pendown()


t.forward(100)


t.right(90)
t.forward(40)


t.backward(40)
t.right(90)
t.backward(50)
t.left(90)
t.forward(35)


t.backward(35)
t.right(90)
t.backward(50)
t.left(90)
t.forward(40)

# Finish
t.hideturtle()
turtle.done()
