# solutions to exercise 4-2

import math
import turtle



def move(t, length):
    """Move turtle t forward by length without leaving a trail."""
    t.pu()
    t.fd(length)
    t.pd()


def polyline(t, length, angle, n):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = (2 * r * math.pi) * (angle / 360)
    n = int(arc_length  / 3)
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, step_length, step_angle, n)


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(90)


def flower(t, petals, r, angle):
    for p in range(petals):
        petal(t, r, angle)
        t.lt(int(360/petals))


if __name__ == '__main__':
    # draw flowers like in exercise
    bob = turtle.Turtle()

    move(bob, -100)
    flower(bob, 7, 100, 30)
    move(bob, 100)
    flower(bob, 10, 60, 45)
    move(bob, 100)
    flower(bob, 15, 200, 10)


turtle.mainloop()
