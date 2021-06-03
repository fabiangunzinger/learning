# solutions to turtle exercises

import math
import turtle

bob = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    circumference = 2 * r * math.pi
    n = int(circumference / 3)
    length = circumference / n
    polygon(t, length, n)


def polyline(t, length, angle, n):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon2(t, length, n):
    angle = 360 / n
    polyline(t, length, angle, n)


def arc(t, r, angle):
    arc_length = (2 * r * math.pi) * (angle / 360)
    n = int(arc_length  / 3)
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, step_length, step_angle, n)


def circle2(t, r):
    arc(t, r, 360)


# arc(bob, 50, 180)
circle2(bob, 90)

turtle.mainloop()
