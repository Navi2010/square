import turtle
wn = turtle.Screen()
gary = turtle.Turtle()
wn.bgcolor("cyan")
gary.pencolor("purple")

for _ in range(4):
    gary.forward(100)
    gary.right(90)

wn.exitonclick()