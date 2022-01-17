

import turtle

scr = turtle.Screen()
scr.bgcolor("black")
scr.title("Vader & Thor")

vader = turtle.Turtle("turtle")
vader.pencolor("purple")
vader.pensize(3)

thor = turtle.Turtle()
thor.pencolor("yellow")
thor.pensize(5)


# square
for x in range(4):

    vader.forward(90)
    vader.left(90)

# triangle

thor.penup()
thor.backward(60)
thor.pendown()
thor.right(120)

for y in range(3):
    
    thor.forward(100)
    thor.left(120)


