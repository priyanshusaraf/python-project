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

win.listen()
win.onkey("w", forward)
win.onkey("a", backward)
win.onkey("s", left)
win.onkey("d", right)
win.exitonclick()
