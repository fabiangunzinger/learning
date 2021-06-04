# solutions to exercise 4-2

import math
import turtle



def move(t, length):
    """Move turtle forward by length without leaving a trail."""
    t.pu()
    t.fd(length)
    t.pd()


def polyline(t, length, angle, n):
    """Draw n line segments with angle between them."""
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    """Draw arc with the given radius and angle."""
    arc_length = (2 * r * math.pi) * (angle / 360)
    n = int(arc_length  / 4) + 3
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, step_length, step_angle, n)


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle):
    for p in range(n):
        petal(t, r, angle)
        t.lt(int(360/n))


if __name__ == '__main__':
    # draw flowers like in exercise
    bob = turtle.Turtle()

    move(bob, -100)
    flower(bob, 7, 60.0, 60.0)

    move(bob, 100)
    flower(bob, 10, 40.0, 80.0)

    move(bob, 100)
    flower(bob, 20, 140.0, 20.0)


turtle.mainloop()
