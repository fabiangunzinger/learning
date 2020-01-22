

# ---------- Recursion ---------- #

# Basic case
def factorial_recursive(n):
	# Base case: 1! = 1
	if n == 1:
		return 1
	# Recursive case: n! = n * (n-1)!
	else:
		print(n)
		return n * factorial_recursive(n-1)
factorial_recursive(5)

# Maintain a state 1
def sum_recursively(current_number, accumulated_sum):
	if current_number == 11:
		return accumulated_sum
	else:
		print(current_number, accumulated_sum+current_number)
		return sum_recursively(current_number + 1, accumulated_sum + current_number)

sum_recursively(1, 0)



houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]
# Each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)
    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]
        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

deliver_presents_recursively(houses)


# Basic cases

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)
factorial(55)

def sum_1_to_b(b):
	if b == 1:
		return 1
	else:
		return b + sum_1_to_b(b - 1)
sum_1_to_b(3)

def sum_a_to_b_down(a, b):
	''' Calculates the sum as sum(a, b) = b + sum(a, b-1) = ... '''
	if b == a:
		return a
	else:
		return b + sum_a_to_b_down(a, b - 1)
sum_a_to_b_down(10, 11)

def sum_a_to_up(a, b):
	''' Calculates the sum as sum(a, b) = a + sum(a + 1, b) = ... '''
	if a == b:
		return b
	else:
		return a + sum_a_to_up(a + 1, b)
sum_a_to_up(10, 11)


# Maintaining states

def factorial_with_state(n, current_value):
	''' Calculates n! by threading the state through each recursive call. '''
	if n == 1:
		return current_value
	else:
		return factorial_with_state(n - 1, current_value * (n - 1) )
factorial_with_state(5, 5)

current_number = 5
accumulated_product = 5
def factorial_with_global():
	''' Calculates n! by using a global state variable. '''
	global current_number
	global accumulated_product
	if current_number == 1:
		return accumulated_product
	else:
		accumulated_product *= (current_number - 1)
		current_number -= 1
		return factorial_with_global()
factorial_with_global()		


# Using cache values

def fibonacci_naive(n):
	''' Calculates values for each n up to n-2 twice in each call and in every call.'''
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_naive(n-1) + fibonacci_naive(n-2)
fibonacci_naive(7)

from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci_with_cache(n):
	''' Caches already calculated values '''
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_naive(n-1) + fibonacci_naive(n-2)
fibonacci_with_cache(7)




# ---------- Sorting sequences ---------- #

a = [1, 2, 5, 3, 7, 8, 6, 4]

def bubble_sort(a):
	for i in range(len(a) -1):
		for j in range(len(a) -1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
	return a
bubble_sort(a)

def merge_sort(a):
	if len(a) < 2:
		return a

	mid = len(a) // 2
	left = merge_sort(a[:mid])
	right = merge_sort(a[mid:])

	result = []
	i = j = 0
	while i < len(left) and j < len(right):
	    if left[i] < right[j]:
	        result.append(left[i])
	        i += 1
	    else:
	        result.append(right[j])
	        j += 1
	result += left[i:]
	result += right[j:]
	return result
merge_sort(a)