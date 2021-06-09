"""
Practice functions for recurion problems.

"""

def countdown(n):
    """Count down from n."""
    if n <= 0:
        print('boom')
    else:
        print(n)
        countdown(n-1)


def fib(n):
    """Return the nth element of the Fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib2(n):
    memory = dict()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n not in memory:
        memory[n] = fib(n-1) + fib(n-2)
    return memory[n]



def factorial(n):
    """Return the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


countdown(5)
print(fib(10))
print(factorial(5))
print(fib2(20))
