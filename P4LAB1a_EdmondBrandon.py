import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.pensize(2)

# Draw a square using a while loop
t.color("blue")
sides = 0
while sides < 4:
    t.forward(100)
    t.right(90)
    sides += 1

# Draw a triangle using a while loop
t.color("red")
sides = 0
while sides < 3:
    t.forward(100)
    t.left(120)
    sides += 1

# Finish
turtle.done()