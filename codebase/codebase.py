#!/usr/bin/env python


###############################################################################
# Basics and best practices
###############################################################################


#############
# Code style
#############


import this

"""Based on https://www.python.org/dev/peps/pep-0008/

Online checker: http://pep8online.com


Math operators
---------------
2*3 - 1

x*x + y*y

(a+b) * (c-d)

Trailing commas
----------------

files = [
    'text.txt',
    'dir.csv',
    ]


"""

# EAFP > LBYL

# EAFP (“it’s easier to ask for forgiveness than permission”) means that you should just do what you expect to work and if an exception might be thrown from the operation then catch it and deal with that fact. What people are traditionally used to is LBYL: “look before you leap”, where you first check whether something will succeed and only proceed if you know it will work.

def dont(m, n):
    if n == 0:
        print("Can't divide by 0")
        return None
    return m / n

def do(m, n):
    try:
        return m / n
    except ZeroDivisionError:
        print("Can't divide by 0")
        return None




###########################################################
## Misc.
###########################################################

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values (from: https://learnxinyminutes.com/docs/python3/)
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal

# Python has a print function
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
print("Hello, World", end="!")  # => Hello, World!

# if can be used as an expression
"yahoo!" if 3 > 2 else 2  # => "yahoo!"

# Shallow copy, copy, deepcopy
# See here: https://stackoverflow.com/questions/
# 2612802/how-to-clone-or-copy-a-list)

import copy
a = [1, 2, 3]
b = a                 # Shallow copy
c = a.copy()          # Copy
d = a[:]              # Copy
e = list(a)           # Copy
f = copy.copy(a)      # Copy
k = copy.deepcopy(a)  # Deep copy (preserves class instance values in list)

b is a
c is a
k is a


# Line continuation

my_very_big_string = (  # Split string
    "For a long time I used to go to bed early. Sometimes, "
    "when I had put out my candle, my eyes would close so quickly "
    "that I had not even time to say “I’m going to sleep.”"
)

from some.deep.module.inside.a.module import (  # Use parentheses
    a_nice_function, another_nice_function, yet_another_nice_function)

# Need to break lines often a sign that you're trying to do too much at once,
# refactor code if possible!



#############################################################
## Modules (from https://learnxinyminutes.com/docs/python3/)
#############################################################

# You can import modules
import math
print(math.sqrt(16))  # => 4.0

# You can get specific functions from a module
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

# You can import all functions from a module.
# Warning: this is not recommended
from math import *

# You can shorten module names
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

# Python modules are just ordinary Python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.

# You can find out which functions and attributes
# are defined in a module.
import math
dir(math)

# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries.


#######################################
# Data model - everything is an object
#######################################


# Everything is an object
isinstance(4, object)       # => True
isinstance([1, 2], object)  # => True

# Objects have identity
id(4)  # => 4501558496 (e.g.)

# Objects have type
type(4)                      # => int
isinstance(type(4), object)  # => Types are also objects

# Objects have value
(41).__sizeof__()  # => 28 (bytes)

# Variables are references to objects
x = 4
y = x
x == y  # => True (both refer to object 4)

# Duck typing (if it walks, swims, and quacks like a duck...)
def compute(a, b, c):
    return (a + b) * c
compute(1, 2, 3)
compute([1], [2, 3], 4)
compute('lo', 'la', 3)


##################
# Data structures
##################

# Integers and floats
5
5.0      # =>      (float)
5 / 2    # => 2.5  (division)
5 // 2   # => 2    (integer division)
5 % 2    # => 1    (modulo operator)

# String
'A string literal'
word = 'Just some word'   # word is a variable that points to a string
word[::-1].lower()
word.find('so')           # => 5
word.startswith('Wo')     # => False
word.isalpha()            # => False (due to spaces)
word.strip('Just some ')  # => 'word'

list(word)    # Casting to a list
word.split()
'-'.join(['Just', 'some', 'word'])

'{} {}'.format('Hello', 'world')
'{0} {1}, {0}'.format('Hello', 'world')
'{greeting}, {name}'.format(greeting='Hello', name='world')
'{} squared is {}'.format(5, 5**2)
'{:2.1f} squared is {:2.2f}'.format(5, 5**2)
# {:{padding_pattern}{alignment - <, ^, >}{padding}}
'{:^12}'.format('Hello')
'{:*^12}'.format('Hello')
'{:->12}'.format('Fab')

name = 'Fabian'
f'{name} is {len(name)} characters long' # Formatted strings - f-strints

# Boolean

# Array


# List
# is a finite, ordered, mutable sequence of elements

a = [1, 2]
a.append([3, 4])  # => [1, 2, [3, 4]] (append single element)

a = [1, 2]
a.extend([3, 4])  # => [1, 2, 3, 4]   (append all elements of iterator)

1 in a    # => True
'1' in a  # => False (string is not in a)

a = [1, 2, 3]
del a[2]     # Remove element from list by index
a.remove(1)  # Remove element from list by value (first ocurrance)
a.pop(1)     # => 2 (remove element by index and return)


# Tuple
# is a finite, ordered, immutable sequence of elements
# (frozen sequence of objects)

a = 'Hello'
b = 'World'
c = a, b
type(c)  # => tuple

# You can also do extended unpacking

*start, a = [1, 2, 3]
a, *middle, c = [1, 2, 3, 4]
a, *rest = [1, 2, 3]
a, _, c = [1, 2, 3]           # Create an ignored variable unneeded stuff


# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6  # tuple 4, 5, 6 is unpacked into variables d, e and f

b, a = c  # Swapping values (can also do directly: b, a = a, b)

type((1))   # => int
type(())    # => tuple
type((1,))  # => tuple



def fibonacci(n):
    """Print out the first n Fibonacci numbers"""
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

fibonacci(4)

for i, name in enumerate(['Fabian', 'Molly']):
    print(i, name)


# Dictionary

a = {'cs': [41, 106], 'econ': [101, 1003]}
b = dict(cs=[41, 106], econ=[101, 1003])
a == b

print(a.get('cs'))
print(a.get('cs', []))    # Use default value for keys not in dict
print(a.get('math', []))  # Returns default value

b.pop('cs')
b.pop('math', None)
del b['econ']

a.keys()    # => <['cs', 'econ']>
a.values()  # => <[[41, 106], [101], [1003]]
a.items()   # => <[('cs', [41, 106]), ('econ', ['101', '1003'])]

for key, value in a.items():
    print(key, value)

for key in a:
    print(key, a[key])

keylist = list(a.keys())

# Set and frozenset
# Is an unordered, finite collection of distinct, hashable elements.

s = set('mississippi')
s.add('b')
s.remove('i')   # KeyError if 'i' is not in set
s.discard('i')  # Same as remove, but no error
s.clear()       # Remove all elements

a = set('ab')
b = set('bc')
a - b  # => {'a'}            (set difference)
a | b  # => {'a', 'b', 'c'}  (set union)
a & b  # => {'b'}            (set intersection)
a ^ b  # => {'a', 'c'}       (symmetric difference)

a < b   # Strict subset
a <= b  # Subset or equal to
a > b   # Strict superset
a >= b  # Superset or equal to

efficient_letters = 'aklmeficntzy'


def is_efficient(word):
    for letter in word:
        if letter not in efficient_letters:
            return False
    return True


is_efficient('efficient')


def is_efficient(word):
    return set(word) <= set(efficient_letters)


is_efficient('efficient')


# File



###############
# Control flow
###############


# Zero values and empty data structures are 'falsy', everything
# else is 'truthy'
bool(False)    # => False
bool([])       # => False
bool(42)       # => True
bool([1, 2,])  # => True

unicorns = ['ha']
if unicorns:
    print("We're in luck!")
else:
    print('No unicorns!')

# Deal with errors for as long as required.
while True:
    try:
        n = int(input('How many unicorns would you like? '))
        break
    except ValueError:
        print('Invalid input. Try again and enter an integer.')

# Deal with multiple errors
try:
    dangerous_code()
except SomeError:
    handle_error()
except (OneError, OtherError):
    handle_multiple_errors()


# Use errors to handle control flow (use below instead of checking
# that file exists)
import os
try:
    os.remove('filename')
except FileNotFoundError:
    pass



########
# Loops
########


for item in iterable:
    process(item)

for n in range(1, 5):
    if n == 3:
        break           # Interrupts loop
    print(n)

for n in range(1, 5):
    if n in [2, 3]:
        continue        # Skips to next iteration
    print(n)

question = ['name', 'quest', 'favourite color']
answer = ['Lancelot', 'the holy grail', 'blue']
for q, a in zip(question, answer):
    print('What is your {}? It is {}.'.format(q, a))

basket = ['pear', 'apple', 'banana', 'apple']
for f in sorted(set(basket)):
    print(f)

while condition:
    do_stuff()

n = 2
while n < 10000:
    print(n)
    n **= 2



#################
# Comprehensions
#################


[fn(x) for x in iterable if cond(x)]

# List comprehension

[n**2 for n in range(10)]
[n**2 for n in range(10) if n**2 < 50]
[n**2 if n**2 < 50 else 0 for n in range(10)]

[(a, b) for a in range(5) for b in range(3)]     # Permutations
[[col for col in range(5)] for row in range(5)]  # Create a matrix

# Dict comprehensions

{key_fun(x): val_fun(x) for x in iterable}

{num: -num for num in range(9)}


# Set comprehensions

{fun(x) for x in iterable}


[n + (n + 1) for n in [0, 1, 2, 3]]
[n % 3 == 0 for n in [3, 8, 9, 5]]
[e[0].upper() for e in ['apple', 'orange', 'pear']]
[(e, len(e)) for e in ['apple', 'orange', 'pear']]



###########################################################
## Functions
###########################################################

""" Aside: parameter passing paradigms

(Mainly based on: https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/)

A variable is a container that points to an object in memory: in a = [] the variable a points to the empty list, but it is not itself the empty list. Can think of variables as boxes we put objects into.

Below two functions help understand the difference.

def reassign(list):
    list = [0, 1]

def append(list):
    list.append(1)

Pass-by-reference:
------------------
The variable, rather than its content, is passed to the function (and content implicitly comes withi it).

mylist = [0]
reassign(mylist)
mylist  # => [0, 1]

mylist = [0]
append(mylist)
mylist  # => [0, 1]

Pass-by-value:
---------------
The object, rather than the variable, is passed to the function (precisely: the function receives a copy of the objects, which are stored separately in memory, and effectively creates its own box, or variable, to put them into). Hence, outside the function, nothing happens to the original object.

mylist = [0]
reassign(mylist)
mylist  # => [0]

mylist = [0]
append(mylist)
mylist  # => [0]

Python: pass-by-object-reference:
----------------------------------

mylist = [0]
reassign(mylist)
mylist  # => [0]

mylist = [0]
append(mylist)
mylist  # => [0, 1]

"""

# Basics

def fn_name(param1, param2):
    value = do_something()
    return value


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
is_prime(262)
is_prime(263)

def echo(n):
    def inner_echo(word):
        return word * n
    return inner_echo
twiceEcho = echo(2)
twiceEcho('Fab')


def ask_yn(prompt,
           retries=4,
           complaint='Enter Y of N!'):
    for i in range(retries):
        ans = input(prompt)

        if ans in 'yY':
            return True
        if ans in 'nN':
            return False

        print(complaint)

ask_yn('Ok to overwrite?')


# Lambda functions

echoLambda = (lambda word, n: word * n)
echoLambda(5, 'Fab')

(lambda word, n: word * n)('Mo', 5)

letters = ['a', 'b', 'c']
shouts = list(map(lambda l: l + '!!!', letters))
print(shouts)


# Variadic positional arguments

def scaled_sum(*args, scale=1):
    return scale * sum(args)

scaled_sum(1, 2, 3)
scaled_sum(1, 5)
scaled_sum(1, 5, scale=10)


# Unpacking variadic positional arguments (to get sum of primes < 100)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = [p for p in range(1, 100) if is_prime(p)]
scaled_sum(*primes)  # '*' unpacks iterables inside function


# Variadic keyword arguments

def stylize_quote(quote, **speaker_info):
    print('> {}'.format(quote))
    print('-' * (len(quote) + 2))

    for k, v in speaker_info.items():
        print('{}: {}'.format(k, v))

stylize_quote(
    'It music be the food of love, play on.',
    act=1,
    scene=1,
    playwright='Shakespeare'
)

# Unpacking variadic keyword arguments

info = {
    'speaker': 'Iron Man',
    'year': 2012,
    'movie': 'The Avengers'
}

stylize_quote('Doth mother know you weareth her drapes?', **info)


# Example

'{0}{b}{1}{a}{0}{2}'.format(
    1, 2, 3, a='b', b='k'    # args = (1, 2, 3), kwargs = {'a': 'b', 'b': 'k'}
)


# More unpacking

def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}

all_the_args(*args)            # equivalent to all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)         # equivalent to all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)


# Function best practices

def my_func():
    """Write a one-line summary here.

    And a more elaborate description from here onwards.
    """
print(my_func.__doc__)


# Function scope

x = 5

def set_x(num):
    # Local var x not the same as global variable x
    x = num    # => 43
    print(x)   # => 43

def set_global_x(num):
    global x
    print(x)   # => 5
    x = num    # global var x is now set to 6
    print(x)   # => 6

set_x(43)
set_global_x(6)

# A bad coding example to highlight the use of unpacking and local scope

def make_complex(*args):
    x, y = args
    return dict(**locals())

make_complex('a', 'b')



########################
# First-class functions
########################

"""
First-Class functions:
"A programming language is said to have first class functions if it treats functions as first-class citizens."

First-Class Citizen (Programming):
"A first-class citizen (sometimes calles first-class object) is an entity which supports all the operations generally available to other entities, such as being being passes as an argument, returned from a function, and assigned to a variable."
"""

# Assign functions to variables

def square(x):
    return x * x

f = square(5)  # Assign function *output* to variable
f = square     # Assign function to variable (no (), as this triggers execution)

print(square)
print(f)       # f points to same object as square
print(f.__name__)

f(5)


# Use functions as arguments in functions

map(lambda x: x**2, [1, 2, 3])
filter(lambda x: x % 2 == 0, [1, 2, 3])

def do_twice(fn, *args):
    fn(*args)
    fn(*args)

do_twice(print, 'Hello world!')


# Return functions from functions

def create_adder(n):
    def adder(m):
        return n + m
    return adder

add_5 = create_adder(5)
print(add_5.__name__)
add_5(10)

# What just happened?
# When calling the create_adder function, we "parametrise" the
# adder function with 10, and then assign it to the add_5 variable.
# Notice that create_adder returns 'adder', rather than 'adder()', so we
# assign the function, rather than the function output to add_5. Also,
# because the output of create_adder is the function adder, assigning
# add_5 to the output of create_adder(5) is the same as assigning it ot the
# adder function 'parametrised' with 5. As seen above, when we assign a
# function to a variable, the variable then points to the same function object
# and thus behaves like the original function.

# Another example

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

paragraph = html_tag('p')
paragraph('This is a paragraph')


###########################################################
## Closures
###########################################################

"""
A closure is an inner function that remembers and has access to variables in the local scope in which it was created, even after the outer function has finished executing.

'A closure closes over the free variables from the environment in which they were creates'.

A free variable is a variable defined inside the scope of the outer function that is not an argument in the inner function. Below, the 'free variable' is message.
"""

def outer(msg):
    message = msg

    def inner():
        print(message)

    return inner

say_hi = outer('hi')
print(say_hi.__name__)
say_hi()                # inner has access to msg outside outer scope.

say_hello = outer('Hello')
say_hello()


# Can make above more concise like so:

def outer(msg):
    def inner():
        print(msg)
    return inner


###########################################################
## Decorators
###########################################################

"""
A special type of function which takes as an argument a function and returns a new function which, usually, wraps some of the behaviour of the supplied function.

Comparison to closures above:
We created an inner function that, once executed, printed the message that was the argument of the outer function. Decorators work in the same way, but execute functions that were passed as arguments in the outer function.
"""

def decorator(original_fn):
    def wrapper():
        return original_fn()
    return wrapper

def display():
    print('Hello world')

decorated_display = decorator(display)

print(decorated_display.__name__)         # Decorated_display points to wrapper

decorated_display()

## What just happened?
## 1) We created a decorator function that takes in a function and returns a
##    wrapper function. The wrapper funciton is not being executed (i.e. has)
##    no () at the end. Once it is executed, it simply returns the original
##    function, as we can see from its definition.
## 2) We then call the decorator with our simple display function as the
##    argument and assign it to the variable decorated_display. decorated_display
##    now points to wrapper, and is ready to be executed. Which we do in the
##    last step.

# Adding additional functionality to wrapper

def decorator(original_fn):
    def wrapper():
        print('Wrapper executed this before {}'.format(original_fn.__name__))
        return original_fn()
    return wrapper

def display():
    print('Hello world')

decorated = decorator(display)
decorated()


## This is already cool. But instead of binding the decorator call to a new
## variable decorated, we can wrap the decorater around the original function
## directly using syntactic sugar like so:

@decorator                        # Equivalent to display = decorator(display)
def display():
    print('Hello world')

display()


# Decorator with args and kwargs

def debug(function):
    def modified_function(*args, **kwargs):
        print('Arguments:', args, kwargs)
        return function(*args, **kwargs)
    return modified_function

@debug
def foo(a, b, c=1):
    return (a + b) * c

foo(2, 3)
foo(2, 3, c=5)



# Decorator for logging

def my_logger(orig_fn):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_fn.__name__),
                        level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs {}'.format(args, kwargs))
        return orig_fn(*args, **kwargs)

    return wrapper

@my_logger
def foo(a, b, c=1):
    return (a + b) * c

foo(1, 2, c=7)    # Creates foo.log with logged info


# Decorator for timing

def my_timer(orig_fn):
    import time

    def wrapper(*args, **kwargs):
        before = time.time()
        result = orig_fn(*args, **kwargs)
        after = time.time()
        delta = (after - before) * 1000
        print('{} ran in {} ms'.format(orig_fn.__name__, delta))
        return result

    return wrapper

import time

@my_timer
def foo(a, b, c=1):
    time.sleep(1)
    return (a + b) * c

foo(1, 2, c=7)


# Chaining decorators

## Try using decorators from above

@my_timer
@my_logger
def foo(a, b, c=1):
    time.sleep(1)
    return (a + b) * c

foo(4, 5)

## Doesn't work, because above creates foo = my_timer(my_logger(foo)), which --
## because my_logger returns 'wrapper' -- is equal to foo = my_timer(wrapper).
## Need to wrap wrappers using functools wrapper like so:

from functools import wraps

def my_logger(orig_fn):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_fn.__name__),
                        level=logging.INFO)

    @wraps(orig_fn)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs {}'.format(args, kwargs))
        return orig_fn(*args, **kwargs)

    return wrapper


def my_timer(orig_fn):
    import time

    @wraps(orig_fn)
    def wrapper(*args, **kwargs):
        before = time.time()
        result = orig_fn(*args, **kwargs)
        after = time.time()
        delta = (after - before) * 1000
        print('{} ran in {} ms'.format(orig_fn.__name__, delta))
        return result

    return wrapper

@my_timer
@my_logger
def foo(a, b, c=1):
    return (a + b) * c

foo(4, 5)


# Decorator for caching (still don't 100 percent understand this)

def cache(fn):
    fn._cache = {}
    def wrapper(*args):
        if args not in fn._cache:
            fn._cache[args] = fn(*args)
#         print(fn._cache, fn._cache[args])
        return fn._cache[args]
    return wrapper

@cache
def fib(n):
    return  fib(n-1) + fib(n-2) if n > 2 else 1

fib(5)


#########################
# Functional programming
#########################

"""

A programming paradigm built on the idea of composing programs of functions,
rather than sequential steps of execution.

Advantages of functional programming
-------------------------------------
- Simplifies debugging
- Shorter and cleaner code
- Modular and reusable code


Memory and speed considerations
--------------------------------
- Map/filter more memory efficient because they compute elements only when called, while list comprehension buffers them all.
- Call to map/filter if you pass lambda comes with extra function overhead which list comprehension doesn't have, which makes the latter usually faster.

"""

# Procedural programming - "program flow"
def get_odds(arr):
    return_list = []
    for elem in arr:
        if elem % 2 == 1:
            return_list.append(elem)
    return return_list

# Functional programming - "programs are sets of functions"
def get_odds(arr):
    return list(filter(lambda elem: elem % 2 ==1, nums))


# Lambda function

"""
Pass as a parameter into other functions to customise their behaviour.
"""

pairs = [(3, 2), (-1, 5), (4, 4), (8, 1)]

max(pairs, key=lambda tup: tup[1])    # Find based on second element

sorted(pairs, key=lambda tup: tup[1]) # Sort by second element


# Map function

"""
Apply a function elementwise to an array and store the result.
"""

def lengths(arr):                         # Procedural
    lengths = []
    for elem in arr:
        lengths.append(len(elem))
    return lengths

def lengths(arr):                         # Using list comprehension
    return [len(elem) for elem in arr]

def lengths(arr):                         # Functional
    return list(map(len, ['fab', 'mo']))



# Filter function

"""
Extract elements of an iterable which fulfill certain criteria.
"""

## Procedural
def starts_with_m(arr):
    return_array = []
    for elem in arr:
        if elem.lower().startswith('m'):
            return_array.append(elem)
    return return_array

## List comprehension
def starts_with_m(arr):
    return [elem for elem in arr if elem.lower().startswith('m')]

## Functional
def starts_with_m(arr):
    return list(filter(lambda elem: elem.lower().startswith('f'), arr))



############
# Iterators
############

"""
Finite or infinite streams of data delivered one value at a time that can be looped over and read into
data structures (if they are finite).
"""

# Filter (and map) create iterators
names = ['Zebra', 'Kangaroo', 'Elephant', 'Cat']
long_names = filter(lambda word: len(word) > 7, names)

for name in long_names:
    print(name)

# Creating an iterator object

toTen = (n for n in range(11))
toTen
next(toTen)
for n in range(10):
    print(n)


# Itertool module

import itertools
import operator

list(itertools.combinations(['a', 'b', 'c'], 2))
list(itertools.permutations(['a', 'b', 'c'], 2))

for el in itertools.permutations('abc', 2):
    print(el, end=', ')

for el in itertools.repeat('Lololo', 5):
    print(el, end='')

print(list(itertools.starmap(operator.mul, itertools.zip_longest([3, 5, 7], [2, 3], fillvalue=1))))



#############
# Generators
#############

"""
Advantages
-----------

Allow us to compute data on demand: avoid expensive function calls and reduce memory buffering.

Allow us to represent infinite streams of data.
"""

def fib(n):                   # Fibonacci sequence as a function...
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a+b

def fib():                    # ... and as a generator
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a

g = fib()  # Namespace created, fib() pushed to stack
next(g)

for _ in range(5):
    print(next(g))


# Lazy generation -- generate Fibonacci sequence on demand

def fibs_under(n):
    for num in fib():
        if num > n:
            break
        print(num)

fibs_under(100)


###########################################################
## Classes
###########################################################

"""
Why use classes?
-----------------
They allow us to logically group our data and functions in a way that's easy to reuse and easy to build upon.

By data and functions we mean attributes and methods; so an attribute is data associated with a specific class, a method is a function associated with a specific class.

Class vs instance of a class:
------------------------------
A class is a blueprint to create instances of that class. In the example below, Employee is the class, each employee is an instance of the class.

Source:
-------
https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=41&t=0s
"""

# Create a simple class

class Employee:

    # Class variables
    raise_amount = 1.04
    num_employees = 0

    # Instance variables
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Increment num_employees each time instance is created
        Employee.num_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Create an instance of the Employee class
emp_1 = Employee('Fabian', 'Gunzinger', 50000)
emp_2 = Employee('Molly', 'Janz', 60000)

# Print attribute and method output for the instance
emp_2.email

emp_1.fullname()           # This automatically gets transformed into below
Employee.fullname(emp_1)

emp_1.apply_raise()
emp_1.pay

emp_1.num_employees

emp_1.__dict__
Employee.__dict__


########
# Numpy
########

import numpy as np


"""
numpy array axes: rows (axis 0), columns (axis 1), depth (axis 2)

Example for axis 2: when data is images, axes 0 and 1 would be pixels, axes 2 would be red, green, blue tuple - i.e. exis 2 would be of dimension 3.
"""

# Build ndarray from iterator

np.array((x*x for x in range(5)))    # Doesn't work
np.fromiter((x*x for x in range(5)), int)

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr
np.sum(arr, axis=0)  # Sum along rows - sums vertically (down along rows)
np.sum(arr, axis=1)  # Sum along axis - sums horizontally (across along columns)




###########
# File I/O
###########

# Navigate directory
import os
cwd = os.getcwd()
os.listdir(cwd)
dataDir = os.path.join(cwd,'../data')

# Ensure that files are closed automatically
from urllib.request import urlopen
with urlopen('http://composingprograms.com/shakespeare.txt') as f:
    text = f.read(200)
text


# Importing data

# Text files

f = open('file.txt')         # Don't do this
a = f.read()
print a
f.close()
Good:

with open('file.txt') as f:  # Do this instead (closes f even if error is raised inside with block)
    for line in f:
        print line

with open('name_of_file.txt', mode='r') as file:
    print(file.read())

with open('name_of_file.txt', mode='r') as file:
    print(file.readline())


# Flat files

df = pd.read_csv(file, sep='\t', header=None, names=col_names,
                 na_values={'col1' : ['-1'], 'col2' : ['999']},
                 parse_dates=[[0, 1, 2]])


# Excel

file = os.path.join(dataDir, 'excel.xlsx')
xlsx = pd.ExcelFile(file)
print(xlsx.sheet_names)
df = xlsx.parse('Sheet1', skiprows=[0], usecols=[0, 2], names=['id', 'urn'])
print(df.head())

# HDF5
import h5py
import os
file = os.path.join(dataDir, 'LIGO_data.hdf5')
data = h5py.File(file, mode='r')
print(type(data))
for key in data.keys():
	print(key)
group = data['strain']
for key in group.keys():
	print(key)
strain = data['strain']['Strain'].value


# Matlab

mat = scipy.io.loadmat('name_of_file.mat')


# SQLite

file = os.path.join(dataDir, 'Northwind_small.sqlite')
print(file)

engine = create_engine('sqlite:///Northwind_small.sqlite')
table_names = engine.table_names()
print(table_names)
print(engine.table_names())

with engine.connect() as con:
	rs = con.execute('SELECT * FROM ...')
	df = pd.DataFrame(rs.fetchall())
	df.columns = rs.keys()

df1 = pd.read_sql_query('SELECT * FROM ...', engine)


print(engine.table_names())
con = engine.connect()
rs = con.execute("SELECT * FROM Orders")


# Web

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
df = pd.read_csv(url, sep=";")
print(df.head())
print(df.keys())
pd.DataFrame.hist(df[['fixed acidity']])
plt.show()

url = 'https://www.python.org/~guido/'
r = requests.get(url)
text = r.text
soup = BeautifulSoup(text)
pretty_soup = soup.prettify()
print(pretty_soup)


# JSON

url = 'http://www.omdbapi.com/?t=hackers&apikey=c534d63b'
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
	print(key + ":", value)



# zip

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

[(l, n) for l, n in zip(letters, numbers)]

for l, n in zip(letters, numbers):
	print(l, n)

print(*zip(letters, numbers))

print(*range(5))

z = zip(letters, numbers)
letters, numbers = zip(*z)
print(letters, numbers)



# Manually creating df from dictionary

data = {'day' : ['Mo', 'Tu'],
		'hour' : [12, 14],
		'training' : ['hiit', 'push']}
df = pd.DataFrame(data)

# Creating df from lists

day = ['Mo', 'Tu']
hour = [12, 14]
training = ['hiit', 'push']
labels = ['day', 'hour', 'type']
cols = [day, hour, training]
data = dict(zip(labels, cols))
df = pd.DataFrame(data)
df.head()


# Importing multiple files

files = ['file1', 'file2']
dfs = [pd.read_csv(f) for f in files]
df = pd.concat(dfs)


# Create new string containing iterables (e.g. for filenames)

files = ["%s_top5.csv" %medal for medal in ['silver', 'gold', 'bronze']]
print(files)


########
# NumPy
########

###############################################################################
###############################################################################
###############################################################################
###                                 Pandas
###############################################################################
###############################################################################
###############################################################################


# Append


# Concatenating

df = pd.concat([df1, df1]) # Row-wise concatenation
df = pd.concat([df1, df1], ignore_index=True) # To reset index
df = pd.concat([df1, df2], axis=1) #Column-wise concatenation
df = pd.concat([df1, df2], axis=1, join='outer') # Default
df = pd.concat([df1, df2], axis=1, join='inner') # Inner joint
# Concatenating many frames using glob module
import glob
csv_files = glob.glob('*.csv')
list_data = [pd.read_csv(file) for file in csv_files]
df = pd.concat(list_data, axis=0) # Concatenate vertically (stack below)
df = pd.concat(list_data, axis=1) # Concatenate horizontally (merge)
# Create multi-level row or column index
rain1314 = pd.concat([rain2013, rain2014], keys=[2013, 2014])
rain1314 = pd.concat([rain2013, rain2014], keys=[2013, 2014], axis='columns')
# Do above but use dict
rain_dict = {2013: rain2013, 2014: rain2014}
rain1314 = pd.concat(rain_dict, axis='columns')


# Merge using join method

df1.join(df2)
df1.join(df2, how='right/inner/outer')


# Merge using merge function

# Can do 1:1, m:1, 1:m by specifying left/right accordingly using the same function
pd.merge(df1, df2)		# Merges on all common columns
pd.merge(df1, df2, on=['v1', 'v2']) # Merge on selected vars using inner join
pd.merge(df1, df2, suffixex=['_df1', '_df2']) # Custom suffixed to identify origin of columns (default is x, y,)
pd.merge(df1, df2, left_on='id1', right_on='id') 	# If id names differ
# Joins
pd.merge(df1, df2, how='left')	# Left join (all rows of left df retained)
pd.merge(df1, df2, how='right')	# Right join (all rows of right df retained)
pd.merge(df1, df2, how='outer') # Outer join, retain union of rows
pd.merge(df1, df2, how='inner')	# Inner join, retain intersection (default)


# Ordered merges

tx_weather_ffill = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus', '_hus'], fill_method='ffill')


# Before merging, use df2 index to reindex df1, and drop values that don't appear in df1 but do in df2.
df1.reindex(df2.index).dropna()
df.sort_index()




# Sorting index

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()
# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)
# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF')
# Reindex weather1 (which is quarterly index) using the list year with forward-fill: weather3
weather3 = weather1.reindex(year).ffill()


# List elements in index

## In hierarchical index
df.index.levels[0]

## If df is a copy from a different index
## This is somewhat weird (and discussed here: https://github.com/pandas-dev/pandas/issues/2770#issuecomment-29547103). If df is a copy of another df, then using df.index.levels returns the index levels of the original index rather than the copy, which is truly weird, but the below is a workaround that works, just need to remember.
df.index.get_level_values(0)



# Stuff that doesn't fit anywhere else

df['new'] = df.old.replace('$', '')
df.columns = ['name of col 1', 'name of col 2']
df['weekday'].unique()		# List of unique values
df['weekday'].nunique()		# Number of unique values
df['weekday'].value_counts() 	# Number of observations per unique value

rowtotals = df.sum(axis='columns')		# Calculating row totals

# Create a Boolean Series that is True when 'Edition' is between 1952 and 1988: during_cold_war
during_cold_war = (medals.Edition >= 1952) & (medals.Edition <= 1988)
# Extract rows for which 'NOC' is either 'USA' or 'URS': is_usa_urs
is_usa_urs = medals.NOC.isin(['USA', 'URS'])
# Use during_cold_war and is_usa_urs to create the DataFrame: cold_war_medals
cold_war_medals = medals.loc[during_cold_war & is_usa_urs]



# Arithmetic with Series and DataFrames

# Divide all columns in df by series s (divide() is more flexible than / )
df1 = df.divide(s, axis='rows')
# Percentage changes
df.pct_change() * 100
# Add data frames with different indexes (so that index values that don't appear in both indexes are not NaN, as they would be if we used bronze + silver + gold)
bronze.add(silver, fill_value=0).add(gold, fill_value=0)

# Convert temps_f to celsius: temps_c and rename columns from F to C
temps_c = (temps_f - 32) * 5/9
temps_c.columns = temps_c.columns.str.replace('F', 'C')



# Inspecting data

df.info()
df.shape
df.columns
df.describe()
df.dtypes
df.columns.value_counts()
df.column.plot('hist')
df.head()
df.tail()
df.sample()


# Setting index

prices = [10, 11, 12, 13, 15]
days = ['Mo', 'Tu', 'We', 'Th', 'Fr']
shares = pd.Series(prices)
shares = pd.Series(prices, index=days)
shares.index.name = 'Weekdays'
shares.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
shares.index.name = 'Long weekdays'
sales = sales.set_index('state')



# Indexing and slicing data frames
# start:stop:stride, with start but without stop, starts at zero.

df['col1']	# Col1 as a series
df[['col1']] # Col1 as a data frame
df['colname']['rowname']
df.colname['rowname']
df.loc['rowname', 'colname']
df.iloc[rowindex, colindex]
df.loc['row1':'row4', 'col2':'col5'] # Rows 1-3 and cols 2-4
df.loc[['row1', 'row2'], ['col1', 'col2']] # Multiple rows and cols
# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election.loc['Perry':'Potter']
# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
p_counties_rev = election.loc['Potter':'Perry':-1]


# Hierarchical indexing

# Set the index to be the columns ['state', 'month'] and sort
stocks = stocks.set_index(['Symbol', 'Date']).sort_index()
stocks.loc['AAPL']
stocks.loc['AAPL':'MSFT']
stocsk.loc[('AAPL', '2016-10-05')]
# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY', 1)]
# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA', 'TX'], 2), :]
# Access the inner month index and look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None), 2), :]
# Create alias for pd.IndexSlice: idx and print all the data on medals won by the United Kingdom
idx = pd.IndexSlice
print(medals_sorted.loc[idx[:, 'United Kingdom'], :])


# Stacking, unstacking, swapping a multi-level indices

# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level='weekday')
# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))




# Filtering

# Create the boolean array: high_turnout and filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout = election.turnout > 70
high_turnout_df = election[high_turnout]
# Assign np.nan to the 'winner' column where the results were too close to call
too_close = election.margin < 1
election.winner[too_close] = np.nan


# Missing values

df = df.dropna()	# Keep rows with no nan only
df[['v1', 'v2']] = df[['v1', 'v2']].fillna(0) 	# Replace nan in v1,v2 with 0
mean = df['var'].mean()	# Replace nan in var with mean of var
df['var'] = df['var'].fillna(mean)
# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)
# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)
# Drop columns in titanic with less than 1000 non-missing values
print(titanic.dropna(thresh=1000, axis='columns').info())


# Transforming data

# Create rounded count of dozens using four methods (best to worst)
df.floordiv(12)
np.floor_divide(df, 12)
df.apply(lambda n: n // 12)
def dozens(n):
	return n // 12
df.apply(dozens)
# Create the dictionary: red_vs_blue and use to map winner to new column color
red_vs_blue = {'Obama':'blue', 'Romney':'red'}
election['color'] = election.winner.map(red_vs_blue)


# Tidy data

# 1. Columns represent separate variables
# 2. Rows represent individual observations
# 3. Observational units form tables


# Melting and pivoting

data = {'treatment': ['A', 'B'],
		'F': [5, 8],
		'M': [3, 9]}
df = pd.DataFrame(data)
print(df)
print(pd.melt(df))
print(pd.melt(df, id_vars='treatment'))
melted = pd.melt(frame=df, id_vars=['treatment'], var_name='gender', value_name='responses')
print(melted)
print(melted.pivot_table(index='treatment',
						values='responses',
						aggfunc=np.sum))
print(melted.pivot_table(index='treatment',
						columns='gender'))
print(melted.pivot_table(index='treatment',
						columns=['gender'],
						values=['responses']))


# Extract elements from variable values using string slicing
df['new'] = df.old.str[0]


# Groupby, aggregation, transformation, filtering

# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')
# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()
# Calculate the max and median of age and fare columns
by_class[['age','fare']].agg(['max', 'median'])
# Print the maximum age in each class
print(aggregated.loc[:, ('age','max')])

# Group gapminder by 'Year' and 'region': by_year_region
by_year_region = gapminder.groupby(['Year', 'region'])
# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()
# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}
# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Outliers in gapminder data
standardized = gapminder_2010.groupby('region')['life', 'fertility'].transform(zscore)
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)
gm_outliers = gapminder_2010.loc[outliers]


# Data types

df['var'] = df['var'].astype(str)
df['var'] = df['var'].astype('category')
df['var'] = df['var'].to_numeric()
df['var'] = pd.to_numeric(df['var'], errors='coerce') # NaN for missing values
numeric = pd.to_numeric(df)		# Entire df to numeric


# Regular expressions

import re
# To match and only match dollar values like $17.89, use '^\d*\.\d{2}$'
# Find all occurrances of pattern in field
matches = re.findall('\d*', '23 texts contain 45 number')
# To apply to an entire column
pattern = re.compile('^\d*\.\d{2}$')
result = pattern.match('$987897.23')
bool(result)


# Mapping

under10 = (titanic['age'] < 10).map({True: 'under 10', False: 'over 10'})


# Using functions to clean data

df.apply(np.mean, axis=0) # Column means
df.apply(np.mean, axis=1) # Row means
def recode_gender(gender):
    if gender == 'Female':
        return 0
    elif gender == 'Male':
        return 1
    else:
        return np.nan
df['recode'] = df.sex.apply(recode_gender)


# Lambda functions

df.apply(lambda x: x ** 2)	# Short way
def my_square(x):			# Long way
    return x ** 2
df.apply(my_square)


# Duplicate data

df = df.drop_duplicates()


# Grouping data

df = gapminder.groupby('year')['life_expectancy'].mean() # Yearly means


# Consistency checks

assert gapminder.year.dtypes == np.int64

countries = gapminder['country']
countries = countries.drop_duplicates()
pattern = '^[A-Za-z\.\s]*$'
mask = countries.str.contains(pattern)
mask_inverse = ~mask
invalid_countries = countries.loc[mask_inverse]
print(invalid_countries)


# Slicing time-series

df = pd.read_csv('file.csv', parse_dates=True, index_col='Date')
# Extract particular time of particular date
df.loc['2018-02-19 11:00:00']
# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = ts0.loc['2010-10-11 21:00:00':'2010-10-11 22:00:00']
# Extract '2010-07-04' from ts0: ts2
ts2 = ts0.loc['2010-07-04']
# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = ts0.loc['2010-12-15':'2010-12-31']


# Setting column headers

# Split on the comma to create a list: column_labels_list
column_labels_list = column_labels.split(',')
# Assign the new column labels to the DataFrame: df.columns
df.columns = column_labels_list
# Remove the appropriate columns: df_dropped
df_dropped = df.drop(list_to_drop, axis='columns')


# Resetting index

# Reset the index of ts2 to ts1 (e.g. to fill holes in ts2 index), and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate('linear')
# Convert the 'Date' column into a collection of datetime objects: df.Date and set the index to be the converted 'Date' column
df.Date = pd.to_datetime(df.Date)
df.set_index('Date', inplace=True)



# Resampling

# Downsample to 6 hour data and aggregate by mean: df1
df1 = df.Temperature.resample('6H').mean()
# Downsample to daily data and count the number of data points: df2
df2 = df.Temperature.resample('D').count()
# Extract temperature data for August: august
august = df.loc['2010-08', 'Temperature']
# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()
# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-08-01':'2010-08-15']
# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()
# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})
# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()
# Population data from decade to yearly
population.resample('A').first().interpolate('linear')


# String methods

# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()
# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')
# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()


# Datetime methods

# Build a Boolean mask to filter for the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'
# Use the mask to subset the data: la
la = df[mask]
# Combine two columns of data to create a datetime series: times_tz_none
times_tz_none = pd.to_datetime(la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'] )
# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')
# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')


# Column formatting

# Pad leading zeros to the Time column: df_dropped['Time']
df_dropped['Time'] = df_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))


# Assert for data checks

assert df.Var.notnull().all()		# Check that Var has no nan values
assert df.notnull().all().all()		# Check that no column in df has any nan
assert pd.notnull(df)				# Alternative to above
assert (df > 0).all().all()			# Check that all values are larger than 0
assert df['country'].value_counts()[0] == 1 # Check that each country has 1 obs
assert df.year.dtypes == np.int64


# Exploratory data analysis

df.describe()
df.mean()
df.varname.mean()
df.median()
df.quantile(.99)
df.quantile([0.05, 0.95])
df.min()
df.value_counts(dropna=False).head()
df.varname.value_counts()

df.mean(axis='columns').plot()



###########
# Plotting
###########

# Style options

style='color''marker''line type' e.g. 'go-:'

# Good to know

# Plotting works best with single-level indexes, so before multi-level index, use unstack() like so:
grouped = df.groupby(['var1', 'var2'])
grouped = grouped.unstack()




# Axes
plt.axes([0.05, 0.05, 0.425, 0.9]) #(plt.axes([xlo, ylo, width, height]))
plt.plot(year, physical_sciences, color='blue')
plt.axes([0.525, 0.05, 0.425, 0.9])
plt.plot(year, computer_science, color='reduce')
plt.show()



# Subplots

# Create a figure with 2x2 subplot layout and make the top left subplot active
plt.subplot(2,2,1)
# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')
# Make the top right subplot active in the current 2x2 subplot grid
plt.subplot(2,2,2)
# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')
# Make the bottom left subplot active in the current 2x2 subplot grid
plt.subplot(2,2,3)
# Plot in green the % of degrees awarded to women in Health Professions
plt.plot(year, health, color='green')
plt.title('Health Professions')
# Make the bottom right subplot active in the current 2x2 subplot grid
plt.subplot(2,2,4)
# Plot in yellow the % of degrees awarded to women in Education
plt.plot(year, education, color='yellow')
plt.title('Education')
# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()


df.plot(subplots=True)
plt.subplots(nrows=2, ncols=1)
# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)
# Plot the PDF on the first line
df.fraction.plot(ax=axes[0], kind='hist', bins=30, normed=True)
# Plot the CDF
df.fraction.plot(kind='hist', bins=30, normed=True)
plt.show()

# Highlighting particular aspects of time series

# Plot the summer data and highlight one week in particular (to plot week separately, use plt.clf() after the first plot).
df.Temperature['2010-Jun':'2010-Aug'].plot()
plt.show()
df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()



# Scatter plots

df.plot(kind='scatter', x='xvar', y='yvar')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.yscale('log')
plt.xlim(0, 45)
plt.ylim(0, 45)

_ = plt.plot(versicolor_petal_length,versicolor_petal_width, marker='.', linestyle='none')
_ = plt.xlabel('Petal length (cm)')
_ = plt.ylabel('Petal width (ch)')



# Line plots / time series

df.loc['2002':'2005', ['open', 'close', 'high', 'low']].plot()
plt.savefig('stocks.png')

plt.plot(aapl, color='blue', label='AAPL')
plt.plot(ibm, color='green', label='IBM')
plt.legend(loc='upper left')
plt.xticks(rotation=60)

# Plot 250 day moving avarage on top of original series
plt.plot(mean_250, color='cyan')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('250d averages')


# Plot the series in the top subplot in blue and 2007-2008 in black below
plt.subplot(2,1,1)
plt.xticks(rotation=45)
plt.title('AAPL: 2001 to 2011')
plt.plot(aapl, color='blue')
view = aapl['2007':'2008']
plt.subplot(2,1,2)
plt.xticks(rotation=45)
plt.title('AAPL: 2007 to 2008')
plt.plot(view, color='black')
plt.tight_layout()


# Histograms

df.plot(kind='hist', y='varname')
df.plot(kind='hist', y='varname', bins=20, range=(1,8)) # Set bins and range
df.plot(kind='hist', y='varname', normed = True) # Norm s.t. area is 1
df.plot(kind='hist', y='varname', cumulative=True normed = True) # A CDF
df.plt.hist('same arguments as for above')
# Histogram and CDF in the same plot
pdf = plt.hist(pixels, bins=64, range=(0,256), alpha=0.4)
plt.grid('off')
plt.twinx()
cdf = plt.hist(pixels, bins=64, range=(0,256),
               cumulative=True, normed=True,
               color='blue', alpha=0.4)
plt.xlim((0,256))
plt.grid('off')
# Customising bin edges
bin_edges = [0, 10, 20, 30, 40, 50]
plt.hist(data, bins=bin_edges)
# Use "square root rule" to determine the number of bins
n_bins = int(np.sqrt(len(varname)))
_ = plt.hist(varname, bins=n_bins)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')
# Advantages
# 1. It's easy and can be informative
# Disadvantages
# 1. Danger of binning bias – number of bins might influence conclusions
# 2. We don't plot all of the data but rather put data into bins
# Potential remedies
# 1. (Bee) swarm plot
# 2. Empirical CDF

# Box plots

df.plot(kind='box', y='yvar')
df.varname.plot(kind='box')
df.boxplot()


# Empirical CDFs (ECDFs)

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n
    return x, y
x_vers, y_vers = ecdf(versicolor_petal_length)
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# ECDF with percentiles overlaid

percentiles = np.array([2.5, 25, 50, 75, 97.5])
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)
_ = plt.plot(x_vers, y_vers, '.')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')
_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',linestyle='none')
plt.show()



# Customising axes

plt.xaxis(lower, upper)
plt.xticks(rotation=45)
plt.yaxis(lower, upper)
plt.axis((xlower, xupper, ylower, yupper))


# Legends

plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
# Add a legend at the lower center
plt.legend(loc='lower center')


# Annotations

# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science')
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='lower right')
# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()
# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]
# Add a black arrow annotation
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max+5, cs_max+5), arrowprops=dict(facecolor='black'))
# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()


# Misc.

plt.savefig('path_and_name.png')		# Save figure
plt.tight_layout()						# Remove white-space


# Contour plots

u = np.linspace(-2,2,30)
v = np.linspace(-1,1,20)
X,Y = np.meshgrid(u, v)
Z = np.sqrt(X**2+Y**2)
K = X+Y
plt.subplot(1,2,1)
plt.contourf(X,Y,Z,20, cmap='coolwarm')
plt.colorbar()
plt.title('Coolwarm')
plt.subplot(1,2,2)
plt.contourf(X,Y,K,20, cmap='magma')
plt.colorbar()
plt.title('Magma')
plt.show()


# 2-D histograms

plt.hist2d(hp, mpg, bins=(20, 20), 			# Rectangular bins
			range=((40, 235), (8, 48)))
plt.colorbar()
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()

plt.hexbin(hp, mpg, gridsize=(15, 12),		# Hexagonal bins
			extent=(40, 235, 8, 48))
plt.colorbar()
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()


# Seaborn
##############################################################################

# Using seaborn
sns.set()

# Requirements
# Data needs to be tidy: columns are features and rows observations.


# Linear regression

sns.lmplot(x='weight', y='hp', data=auto)
sns.lmplot(x='weight', y='hp', data=auto, hue='type')	# Separate lines
sns.lmplot(x='weight', y='hp', data=auto, col='type')	# Column subplots
sns.lmplot(x='weight', y='hp', data=auto, row='type')	# Row subplots

# Scatter plot with first and second-order regressions
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, color='blue', label='order 1')
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, order=2, color='green', label='order 2')
plt.legend(loc='upper right')
plt.show()

# Residual plots

sns.residplot(x='hp', y='mpg', data=auto, color='green')


# Strip plots (univariate distribution of small to medium-sized datasets)

sns.stripplot(y='hp', data=auto)
sns.stripplot(x='cyl', y='hp', data=auto)	# By cyl category
sns.stripplot(x='cyl', y='hp', data=auto, jitter=True, size=3)	# Jittery


# Swarmplot (univariate distribution of small to medium-sized datasets)

sns.swarmplot(y='hp', data=auto)
sns.swarmplot(x='cyl', y='hp', data=auto)	# By cyl category
sns.swarmplot(x='hp', y='cyl', data=auto, 	# Horizontally, with additional hue
	hue='origin', orient='h')


# Violinplots (univariate distribution of larger datasets)

sns.violinplot(y='hp', data=auto)
sns.violinplot(x='cyl', y='hp', data=auto)		# By cyl category

# Overlay violin and strip plot
sns.violinplot(x='cyl', y='hp', data=auto, color='lightgray', inner=None)
sns.stripplot(x='cyl', y='hp', data=auto, jitter=True, size=1.5)


# Joint plots (centre with bivariate relationships and distributions on axes)

sns.jointplot(x='hp', y='mpg', data=auto)
sns.jointplot(x='hp', y='mpg', data=auto , kind='hex/scatter/reg/resid/kde/')


# Pair plots (Matrix of histograms and bivariate relationships)

sns.pairplot(df)
sns.pairplot(auto, hue='origin')	# By origin type
sns.pairplot(auto, kind='reg')		# Regression instead of scatter


# Heat maps

sns.heatmap(cov_matrix)



# Bokeh
##############################################################################

from bokeh.plotting import figure
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
# Add a blue circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica, color='blue', size=10, alpha=0.8)
# Add a red circle glyph to the figure p
p.circle(fertility_africa, female_literacy_africa, color='red', size=10, alpha=0.8)
# Specify the name of the file
output_file('fert_lit_separate_colors.html')
# Display the plot
show(p)

# Line graph with dots to indicate data points
p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')
p.line(date, price)
p.circle(date, price, fill_color='white', size=4)
output_file('line.html')
show(p)


# Statistical exploratory data analysis
##############################################################################

# Calculate basic summary statistics

mean_length_vers = np.mean(versicolor_petal_length)
print('I. versicolor:', mean_length_vers, 'cm')

pcts = np.percentile(df.varname, [25, 50, 75])


# Variance and standard deviation

# The variance is the mean of the squared differences from the mean, the
# std the square root of the variance and in the same units as the data.
# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)
# Square the differences: diff_sq
diff_sq = np.square(differences)
# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)
# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)
# Print the results
print(variance_explicit, variance_np)
# Std
print(np.sqrt(variance_up), np.std(versicolor_petal_length))


# Covariance and Pearson correlation coefficient

# The covariance is the mean of the product of the differences from the means
# of two variables (the difference from the y and x mean for a dot on a
# scatter plot). Hence, if both mean differences are relatively high or low (if the data point is relatively large or small on both axes) for most values, the variables are correlated. Otherwise they are uncorrelated.
# Calculating covariance (via var-covariance matrix)
covar_matrix = np.cov(x, y)
covar = covar_matrix[0,1]
# The Pearson correlation coefficient (rho) is more generally applicable because it is dimensionless. It's the ratio of the covariance and the product of the std of each variable – the ration between variability due to codependence and independent variability (it ranges from -1 to 1 with 0 meaning no correlation).
# Calculating rho
corr_matrix = np.corrcoef(x, y)
rho = corr_matrix[0,1]


# Simulations
##############################################################################


# Create an array with 100,000 random numbers between 0 and 1

np.random.seed(42)
random_numbers = np.empty(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()


# Simulate the number of loan defaults out of 100 loans
# Step 1: Create function for Bernoulli trials
# Step 2: Compute the number of defaults for 1000 simulations
# Step 3: Plot ECDF
# Create a function for Bernoulli trials
def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    n_success = 0
    for i in range(n):
        random_number = np.random.random()
        if random_number < p:
            n_success += 1
# Run 1000 simulations
np.random.seed(42)
n_defaults = np.empty(1000)
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100, 0.05)
# Compute ECDF
x, y = ecdf(n_defaults)		# Uses function from above
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Number of defaults')
_ = plt.ylabel('ECDF')
plt.show()
# Directly draw from binomial distribution instead (above as exercise only)
n_defaults = np.random.binomial(n=100, p=0.05, size=10000)



#-----------------------------------------------------------------------------
# Pandas
# ----------------------------------------------------------------------------

df.columns = ['col1', 'col2']
df.index = ['A', 'B', 'C', 'D']
df.index = df.date
df.index.name = 'date'

cols = ['col1', 'col3']		# keep columns 1 and 3 only
df = df[cols]

# Exporting data

out_csv = 'df.csv'
df.to_csv(out_csv)

out_exls = 'df.xlsx'
df.to_excel(out_exls, index=False)



# Steps to analysing data
###############################################################################

1. Load data
2. Cleaning
3. Graphical EDA (histograms, swarm plots, ECDFs)

# Exercises to remember (and eventually delete)

# Me
def speak_excitedly(message, num_exclamations=0, enthusiasm=False):
    if enthusiasm:
        print(message.upper() + '!' * num_exclamations)
    else:
        print(message + '!' * num_exclamations)

speak_excitedly("let's go Stanford", 2, enthusiasm=True)
speak_excitedly('I love Python')

# Solution

def speak_excitedly(message, num_exclamations=0, enthusiasm=False):
    """Return a message with exclamation points, possibly capitalised."""
    message += '!' * num_exclamations
    if enthusiasm:
        return message.upper()
    return message

speak_excitedly("let's go Stanford", 2, enthusiasm=True)
speak_excitedly('I love Python', 1)


def make_table(key_justify='left', value_justify='right', **table_elements):
    """
    Construct table of key-value pairs specified as keyword arguments.

    More elaborate description with example...
    """

    # Map from human-readable justifications to .format alignmend specifiers
    justification = {
        'left': '<',
        'right': '>',
        'center': '^'
    }
    if key_justify not in justification or value_justify not in justification:
        raise ValueError('Invalid justification specifier. \
                         Choose from {}'.format(list(justification.keys())))

    key_alignment_specifier = justification[key_justify]
    value_alignment_specifier = justification[value_justify]

    max_key_length = max(len(key) for key in table_elements.keys())
    max_value_length = max(len(value) for value in table_elements.values())

    # '| ' + padded_key + ' | ' + padded_value + ' |'
    total_length = 2 + max_key_length + 3 + max_value_length + 2

    print('=' * total_length)
    for key, value in table_elements.items():
        print('| {:{key_align}{key_padding}} | {:{value_align}{value_padding}} |'
              .format(key, value,
                      key_align=key_alignment_specifier,
                      key_padding=max_key_length,
                      value_align=value_alignment_specifier,
                      value_padding=max_value_length
                     )
             )
    print('=' * total_length)

make_table(key_justify='left', value_justify='right',
           name='Fabian',
           surname='Gunzinger',
           fav_movement='Handstand',
          )



# Linear algebra with funcitonal programming


import itertools
import operator

u = [1, 2, 3]
v = [3, 4, 5]

def dot_product(u, v):
    assert len(u) == len(v)
    sum(itertools.starmap(operator.mul, zip(u, v)))

def transpose(m):
    return tuple(zip(*m))

def lazy_transpose(m):
    return zip(*m)


# Create a timeit decorater function

def timeit(fn):
    """Decorater that prints out the duration the function took to execute.

    Arguments:
        fn (function) -- The function to time.
    """

    def modified_fn(*args, **kwargs):
        before = time.time()
        out = fn(*args, **kwargs)
        after = time.time()

        delta = (after - before) * 1000
        print('Function duration: {} ms'.format(delta))

        return out

    return modified_fn

@timeit
def slow_fibbi(n):
    """Use recursion to compute the nth Fibbonacci number slowly.

    Arguments:
        n (int) -- The index of the Fibonacci number to compute.
    """
    fib = lambda n: fib(n-1) + fib(n-2) if n >= 2 else 1
    return fib(n)

@timeit
def fast_fibbi(n):
    """Use a while loop to compute the nth Fibonacci number quickly.

    Arguments:
        n (int) -- The index of the Fibonacci numbter to compute.
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

slow_fibbi(30)
fast_fibbi(30)


# Create a timeit decorater function with iterations

def timeit_iter(num_iterations=1):
    """Decorater that prints out the duration the function took to execute.

    Arguments:
        num_iterations (int) -- The number of times to run the functions.
    """
    def wrapper(fn):
        def modified_fn(*args, **kwargs):
            before = time.time()

            for _ in range(num_iterations):
                out = fn(*args, **kwargs)

            after = time.time()

            delta = (after - before) * 1000 / num_iterations

            print('Average function duration: {} ms for {} iterations'.format(delta, num_iterations))

            return out
        return modified_fn
    return wrapper

@timeit_iter(num_iterations=10)
def fast_fibbi(n):
    """Use a while loop to compute the nth Fibonacci number quickly.

    Arguments:
        n (int) -- The index of the Fibonacci numbter to compute.
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

fast_fibbi(30)


####################
# Acknowledgements
####################

"""
https://stanfordpython.com
https://learnxinyminutes.com/docs/python3/
"""