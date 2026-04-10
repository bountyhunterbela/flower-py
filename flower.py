"""Draw a flower-like mandala pattern using Python's turtle graphics."""
import turtle
sc=turtle.Screen()
sc.bgcolor("black")
sc.title("flower and mandala")
p=turtle.Turtle()
p.pensize(1)
p.pencolor("red")
p.speed(0)
for i in range(18):
    p.circle(i*2)
    p.left(20)

turtle.hideturtle()
turtle.done()