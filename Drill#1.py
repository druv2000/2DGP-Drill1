import turtle

def moveUp():
	turtle.setheading(90)
	turtle.forward(50)
	turtle.stamp()
	turtle.update()

def moveLeft():
	turtle.setheading(180)
	turtle.forward(50)
	turtle.stamp()
	turtle.update()

def moveDown():
	turtle.setheading(270)
	turtle.forward(50)
	turtle.stamp()
	turtle.update()

def moveRight():
	turtle.setheading(360)
	turtle.forward(50)
	turtle.stamp()
	turtle.update()

def resetTurtle():
	turtle.reset()
	turtle.stamp()


turtle.speed(0)
turtle.delay(0)
turtle.tracer(0, 0)

turtle.shape('turtle')
turtle.stamp()

turtle.onkey(moveUp, 'w')
turtle.onkey(moveLeft, 'a')
turtle.onkey(moveDown, 's')
turtle.onkey(moveRight, 'd')
turtle.onkey(resetTurtle, 'Escape')

turtle.listen()
	
turtle.exitonclick()
