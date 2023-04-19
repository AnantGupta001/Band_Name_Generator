from turtle import Turtle, Screen

t = Turtle()
s = Screen()

s.listen()


def move_forward():
    """Move the turtle forward by 10 paces."""
    t.fd(10)


def move_backward():
    """Move the turtle backward by 10 paces."""
    t.bk(10)


def move_counter_clockwise():
    """Move the turtle counter-clockwise (left) by 10 paces."""
    t.left(10)


def move_clockwise():
    """Move the turtle clockwise (right) by 10 paces."""
    t.right(10)


def clear_drawing():
    """Clears the Screen and take back the tutle to the center."""
    t.reset()


s.onkey(key="W", fun=move_forward)
s.onkey(key="S", fun=move_backward)
s.onkey(key="A", fun=move_counter_clockwise)
s.onkey(key="D", fun=move_clockwise)
s.onkey(key="C", fun=clear_drawing)

s.exitonclick()
