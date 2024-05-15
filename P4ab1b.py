import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Initials")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(4)  # Set the turtle's drawing speed

# Set the pen color and size
pen.color("blue")  # Choose your preferred color
pen.pensize(3)     # Choose your preferred pen size

# Draw the initial "K"
pen.penup()
pen.goto(-200, 0)
pen.pendown()
pen.left(90)
pen.forward(100)
pen.backward(50)
pen.right(45)
pen.forward(70)
pen.backward(70)
pen.right(90)
pen.forward(70)
pen.penup()


# Move to draw the initial "D"
pen.color("red")
pen.pensize(20)
pen.penup()
pen.goto(0,-40)
pen.left(135)
pen.backward(90)
pen.pendown()
pen.right(90)
pen.circle(150,180)
pen.left(90)
pen.forward(280)

# Hide the turtle and display the result
pen.hideturtle()
screen.mainloop()
