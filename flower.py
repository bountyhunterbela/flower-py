"""Draw a flower-like mandala pattern using Python's turtle graphics."""
import turtle
sc=turtle.Screen()
sc.bgcolor("black")
sc.title("flower and mandala")
p=turtle.Turtle()
p.pensize(1)
p.pencolor("red")
p.speed(0)

PETAL_COUNT = 18
SIZE_STEP = 2
ROTATION_STEP = 20


def main():
    for i in range(PETAL_COUNT):
        p.circle(i * SIZE_STEP)
        p.left(ROTATION_STEP)


if __name__ == "__main__":
    main()
    turtle.hideturtle()
    turtle.done()