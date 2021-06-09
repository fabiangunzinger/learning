import turtle

def koch(t, n):
    """Draw a Koch curve of length n."""
    if n < 25:
        t.fd(n)
        return
    koch(t, n/3)
    t.lt(60)
    koch(t, n/3)
    t.rt(120)
    koch(t, n/3)
    t.lt(60)
    koch(t, n/3)


def snowflake(t, n):
    """Draw a Koch snowflake."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
koch(bob, 300)

turtle.mainloop()
