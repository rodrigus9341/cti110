

import turtle

scr = turtle.Screen()
scr.bgcolor("yellow")

knight = turtle.Turtle("turtle")
knight.pencolor("green")
knight.pensize(8)


# first intial
knight.backward(90)
knight.forward(90)
knight.left(90)
knight.forward(80)
knight.left(90)
knight.forward(90)
knight.right(90)
knight.forward(80)
knight.right(90)
knight.forward(90)

# last initial
knight.penup()
knight.forward(60)
knight.pendown()
knight.right(90)
knight.forward(160)
knight.backward(160)
knight.left(90)
knight.forward(90)
knight.right(90)
knight.forward(80)
knight.right(90)
knight.forward(90)
knight.left(135)
knight.forward(110)


