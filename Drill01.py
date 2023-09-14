import turtle 


MOVE_DISTANCE = 50

def moveLeft():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(MOVE_DISTANCE)

def moveRight():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(MOVE_DISTANCE)

def moveUp():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(MOVE_DISTANCE)

def moveDown():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(MOVE_DISTANCE)


turtle.shape("turtle")

turtle.onkey(moveLeft, "a")
turtle.onkey(moveLeft, "A")
turtle.onkey(moveRight, "d")
turtle.onkey(moveRight, "D")
turtle.onkey(moveUp, "w")
turtle.onkey(moveUp, "W")
turtle.onkey(moveDown, "s")
turtle.onkey(moveDown, "S")
turtle.onkey(turtle.reset, "Escape")

turtle.listen()

turtle.exitonclick()
