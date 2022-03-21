"""Picasso Style Pig."""

__author__ = "730487849"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of my scene."""
    turtle: Turtle = Turtle()
    x: float = -10
    y: float = 10
    width: float = 50
    ear(turtle, x, y, width)
    face(turtle, x, y)
    nose(turtle, x, y)
    ears(turtle, x, y, width)
    eye_r(turtle)
    eye_l(turtle)
    done()


def ear(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a triangle on the left."""
    turtle.penup()
    turtle.pendown()
    i: int = 0
    turtle.begin_fill()
    turtle.fillcolor("pink")
    while i < 3:
        turtle.right(120)
        turtle.forward(width)
        i += 1
    turtle.end_fill()


def face(turtle: Turtle, x: float, y: float) -> None:
    """Draw the pig's square face."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    i: int = 0
    colormode(255)
    turtle.fillcolor(254, 195, 140)
    turtle.begin_fill()
    while i < 4:
        turtle.forward(150)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def nose(turtle: Turtle, x: float, y: float) -> None:
    """Draw a small rectangele."""
    turtle.penup()
    turtle.goto(50, -20)
    turtle.color(132, 98, 94)
    turtle.pendown()
    i: int = 0
    while i < 4:
        turtle.forward(40)
        turtle.right(90)
        i += 1
    

def ears(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Drawing the ear on the right side."""
    turtle.penup()
    turtle.goto(190, y)
    i: int = 0
    turtle.begin_fill()
    turtle.fillcolor("pink")
    while i < 3:
        turtle.right(120)
        turtle.forward(width)
        i += 1
    turtle.end_fill()
    turtle.pendown()


def eye_r(turtle: Turtle) -> None:
    """Drawing an eye on the right."""
    turtle.penup()
    turtle.goto(100, -10)
    turtle.pendown()
    turtle.circle(5)


def eye_l(turtle: Turtle) -> None:
    """Drawing an eye on the left."""
    turtle.penup()
    turtle.goto(50, -10)
    turtle.pendown()
    turtle.circle(5)


if __name__ == "__main__":
    main()
