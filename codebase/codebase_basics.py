

# Testing for multiple flags at once

x, y, z = 0, 0, 0

if x == 1 or y == 1 or y == 1:
	print('passed')
else:
	print('failed')

if 1 in (x, y, z):
	print('passed')
else:
	print('failed')

if x or y or z:
	print('passed')

if any((x, y, z)):
	print('passed')


# get() on dicts with default 

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

>>> greeting(382)
"Hi Alice!"

>>> greeting(333333)
"Hi there!"


# Namedtuples

# Using namedtuple is way shorter than
# defining a class manually:
>>> from collections import namedtuple
>>> Car = namedtuple('Car', 'color mileage')
# Our new "Car" class works as expected:
>>> my_car = Car('red', 3812.4)
>>> my_car.color
'red'
>>> my_car.mileage
3812.4
# We get a nice string repr for free:
>>> my_car
Car(color='red' , mileage=3812.4)