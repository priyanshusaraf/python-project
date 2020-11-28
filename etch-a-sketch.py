import turtle

win = turtle.Screen()
turt = turtle.Turtle()

def forward():
  turt.forward(10)

  
def backward():
  turt.backward(10)

  
def left():
  turt.left(10)

  
def right():
  turt.right(10)

  
def undo():
    turt.undo()

    
def clear():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()


win.listen()
win.onkey(key="w", fun=forward)
win.onkey(key="s", fun=backward)
win.onkey(key="a", fun=left)
win.onkey(key="d", fun=right)
win.onkey(key="u", fun=undo)
win.onkey(key="c", fun=clear)
win.exitonclick()
