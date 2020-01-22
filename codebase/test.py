

# Roman numeral helper
# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

class RomanNumerals(object):

	def __init__(self, roman, integer):
		self.roman = roman
		self.integer = integer

	def to_roman(integer: int):

	def from_roman(roman: str):

integer = 2019

l = list(reversed(list(enumerate(reversed(str(integer))))))

[n + i*str(0) for i, n in l if n != '0']


'''
1		I
5		V
10		X
50		L
100		C
500		D
1000	M
'''


class Meal(object):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def sayname(self):
    	print('The meal is called ' + self.name)




# Regex to validate password

import re

# Check that password alphanumeric with one number, upper, and lower.
pw = 'asldad3A'
pattern = '^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])[a-zA-Z\d]{6,}$'
re.findall(pattern, pw)
#Use compile and verbose to do the same but more readable
regex = re.compile("""
	^				# Beginning of string
	(?=.*\d)		# At least one digit
	(?=.*[A-Z])		# At least one upper-case letter
	(?=.*[a-z])		# At least one lower-case letter
	[a-zA-Z0-9]		# Alphanumeric characters only
	{6,}			# At least six
	$				# End of string
	""", re.VERBOSE)
if regex.fullmatch(pw):
	print('Match')
else:
	print('No match')



# Check for alphanumeric character
password = 'hello world'
#Shortest solution
password.isalnum()

# My solution
nums = [chr(n) for n in range(48, 58)]
upper = [chr(n) for n in range(65, 91)]
lower = [chr(n) for n in range(97, 123)]
allowed = set(nums + upper + lower)
all([c in allowed for c in password]) if len(password) > 0



# The hashtag generator

s = 'Codewars is nice'
tag = s.title().replace(' ', '')
if len(tag) > 139:
	return False
else:
	return '#' + tag


# Reverse integer

x = 123
int(''.join(reversed(str(x))))


# Two sums

# In list of numbers find pair of indices for numbers that sum to target

nums = [2, 7, 11, 15]
target = 9

# Brute force is O(n^2)
for n in nums:
	for m in nums:
		if n + m = target and n != m:
			return [nums.index(n), nums.index(m)]

# Below uses hash table and is of complexity O(n)
nums = [2, 7, 11, 15]
target = 9
h = {}
for i, n in enumerate(nums):
	diff = target - n
	if diff in h:
		print([h[diff], i])
	else:
		h[n] = i


# File input

import fileinput
name = input('What is your name? ')


# Ranson note (like scramblies)

magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note = ['give', 'one', 'grand', 'today']
from collections import Counter
print('Yes' if len(Counter(note) - Counter(magazine)) == 0 else 'No')


# Sorting sequence

s = [8, 7, 1, 3, 6, 4, 5, 2, 9]

def merge_sort(a):
	swaps = 0
	if len(a) < 2:
		print('Single value')
		print(a)
		return a
	mid = len(a) // 2
	left = merge_sort(a[:mid])
	right = merge_sort(a[mid:])

	print('Left and right are:')
	print(left, right)

	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		print('Pre swap result is :')
		print(result)
	    if left[i] < right[j]:
	        result.append(left[i])
	        i += 1
	    else:
	        result.append(right[j])
	        j += 1
	    print('Post swap result is :')
		print(result)
	result += left[i:]
	result += right[j:]
    print('Post append result is :')
	print(result)
	return result

merge_sort(s)




# Number of unique meals

class Meal(object):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def sayname(self):
    	print('The meal is called ' + self.name)

m1 = Meal('Basic Burger', ['Lettuce', 'Tomato', 'Onion', 'Patty'])
m2 = Meal('Cheese Burger', ['Cheese', 'Tomato, Patty, Lettuce'])
m3 = Meal('Chef Burger', ['Tomato', 'Patty', 'Onion', 'Lettuce'])
meals = [m1, m2, m3]

unique_meals = len(set([frozenset(m.ingredients) for m in meals]))

print('Number of unique meals: ' + str(unique_meals))




# Queuing bribes

q = [1, 2, 5, 3, 7, 8, 6, 4]

def merge_sort(a):
	swaps = 0
	if len(a) < 2:
		return swaps

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
	        swaps += 1
	result += left[i:]
	result += right[j:]
	return swaps


# Shift arrays
# Shift array a d times to the left
a = [1, 2, 3, 4, 5]
d = 4
a[d:] + a[:d]


# Hourglass sums
arr = [
[-9, -9, -9,  1, 1, 1],
[ 0, -9,  0,  4, 3, 2],
[-9, -9, -9,  1, 2, 3],
[ 0,  0,  8,  6, 6, 0],
[ 0,  0,  0, -2, 0, 0],
[ 0,  0,  1,  2, 4, 0]]
def hourglass_sum(i, j, arr):
	return sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
max([hourglass_sum(i, j, arr) for i in range(4) for j in range(4)])


# Infinite sequence
# Count occurrences of a in first n letters of infinite sequence s.
s = 'abcace'
n = 23
full = (n//len(s))
extra = (n - full*len(s))
s.count('a') * full + s[:extra].count('a')


# Jumping on clouds
# Get from 0 to len(c) by as few jumps as possible. Can jump only on zeroes, and take jumps of max lenth 2.
c = '0 0 0 0 1 0'.split()
current = 0
jumps = 0
while current < len(c) - 1:
	jumps += 1
	if current + 2 >= len(c):
		current += 1
	elif c[current + 2] == 1:
		current += 1
	else:
		current += 2
jumps


# Count valleys
n = 8
s = 'UDDDUDUU'
count = 0
vals = 0
for c in s:
	if c == 'U':
		count += 1
	elif c == 'D' and count == 0:
		count -= 1
		vals += 1
	else:
		count -= 1
vals


# Sum of pairs

ints = [1, 4, 8, 7, 3, 15]
s = 8

yind = 0
xind = 0
for i, x in enumerate(ints):
	for j, y in enumerate(ints[i+1:]):
		if x + y == s:
			if yind == 0:
				xind, yind = i, j+i+1
			elif j+i+1 < yind:
				xind, yind = i, j+i+1
print([ints[xind], ints[yind]])


solutions = []
for i, x in enumerate(ints):
	for j, y in enumerate(ints[i+1:]):
		if x + y == s:
			solutions.append([[x, y], [i, j+i+1]])
min(solutions, key=lambda x: x[1][1])[0]

l = [ [[x, y], j+i+1] for (i, x) in enumerate(ints) for (j, y) in enumerate(ints[i+1:]) if x + y == s]

return min(l, key=lambda x: x[1][1])[0] if l else None


# Primes in numbers 
# Return prime decomposition of n
n = 7775460

# Scramblies
# Check whether s2 can be formed from s1
s1 = 'javascrihello'
s2 = 'javascript'
# Best practice solution
for c in set(s2):
    if s1.count(c) < s2.count(c):
        print(False)
print(True)
# Clever solution
# Counter basically creates a dictionary of counts and letters
# Using set subtraction, we know that if anything is left over,
# something exists in s2 that doesn't exist in s1
from collections import Counter
len(Counter(s2) - Counter(s1)) == 0
# My solution 1 (or without defining lists first)
l1 = sorted(list(s1))
l2 = sorted(list(s2))
all([l1.count(a) >= l2.count(a) for a in l2])
# My solution 2
l1 = sorted(list(s1))
l2 = sorted(list(s2))
try:
	for a in l2:
			l1.remove(a)
except ValueError:
	return False
return True


# Is my friend cheating
# Remove a, b from sequence such that a*b = sum of sequence without a and b.
# My solution is best solution :-)
n = 400
solutions = []
seq = list(range(1, n+1))
seq_sum = sum(seq)
for a in seq:
	b = (seq_sum - a) / (a + 1)
	if b.is_integer() and b <= n:
		solutions.append((a, int(b)))
solutions


# Timeit
timeit.timeit('[a for a in range(4)]', number=1000)

# Flatten a list of lists (remove empty lists)
n = 5
seq = list(range(1, n+1))
l = [[((a, b)) for b in seq if a*b == sum(seq) - a - b] for a in seq]
l
[item for sublist in l for item in sublist]
# or
list(filter(None, l))

# First non-repeating character
string = 'Moo7nmen'
string_lower = string.lower()
for i, letter in enumerate(string_lower):
    if string_lower.count(letter) == 1:
        return string[i]
return ""
# My solution
counts = [list(string.lower()).count(e) for e in list(string.lower())]
string[counts.index(1)] if 1 in counts else ''

# Write number in expanded form
num = 2030405
num = list(str(num))
 ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
# My solution
l = list(reversed(list(enumerate(reversed(str(num))))))
' + '.join([n + i*str(0) for i,n in l if int(n) > 0])

# Maximum subarray sum
arr = [1, -3, 3, -1, 2, -5]
high = curr = 0
for x in arr:
    curr += x
    if curr < 0:
    	curr = 0
    elif curr > high:
    	high = curr
    print(curr, high)
high

# Pete, the baker
recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
min([available.get(k, 0)//recipe[k] for k in recipe])

# Title case
title, minor_words = 'a clash of KINGS', 'a an the of'
title = title.capitalize().split()
minor_words = minor_words.lower().split()
' '.join([word if word in minor_words else word.capitalize() for word in title])

# Order weights by sum of integer components (and, if this is the same, by string order, which is reason for the inner sorted() call)
strng = "101 123 9009 4444 99 2000"
' '.join(sorted(sorted(strng.split()), key=lambda x: sum(int(c) for c in x)))
	
# Give change
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

people = [25, 50, 25, 100]
bills = []
errors = []
for p in people:
	bills.append(p)
	if p == 100:
		bills.remove(50) if 50 in bills else errors.append(False)
		bills.remove(25) if 25 in bills else errors.append(False)
	if p == 50:
		bills.remove(25) if 25 in bills else errors.append(False)
"YES" if all(errors) else "NO"


# Order string (incomplete)

sentence = 'g3ood 4of the2 pe6ople th5e Fo1r'
order = [int(c) - 1 for c in sentence if c.isdigit()]
tuples = [(w,o) for w, o in zip(order, sentence.split())]
tuples.sort()
' '.join([w[1] for w in tuples])

" ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

sentence = 'g3ood 4of the2 pe6ople th5e Fo1r'

sorted(sentence.split(), key = lambda x: int(list(filter(lambda x: x.isdigit(), sentence))[0]))

[int(list(filter(lambda x: x.isdigit(), s))[0]) for s in sentence.split()]


# Filter
word = 'g4dsf'
int(list(filter(lambda x: x.isdigit(), word))[0])

n = range(-5, 5)
m = list
(filter(lambda x: x < 0, n))

a = ['a', '4']
list(filter(lambda x: x.isdigit(), a))


filter('4hel', a)

list(filter(str.isdigit, sentence.split()))

[int(s.isdigit()) for s in sentence.split()]

for idx, (o, w) in enumerate(list):
	print('index is %s, order is %s, word is %s' % (idx, o, w))


# Slice square
https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python

# Convert strings to weird case
string = 'This is a test'
' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word)]) for word in string.split()])

def to_weird_case_word(word):
	return ''.join([c.upper() if i % 2 == 0 else c for i, c in enumerate(word.lower())])
def to_weird_case(string):
	return ' '.join([to_weird_case_word(word) for word in string.split()])
to_weird_case(string)

# Length of shortest word
s = "bitcoin take over the world maybe who knows perhaps"
min([len(w) for w in s.split()])

# Filter out strings from list
l = [1,2,'a','b']
[e for e in l if not isinstance(e, str)]

# Find position of number that differs in evenness
numbers = "2 4 7 8 10"
e = [int(i) % 2 == 0 for i in numbers.split()]
e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

# Different element in list (not correct)
arr = [ 1, 1, 1, 2, 1, 1 ]
m = 0
while arr[m] == arr[m+1]:
	m += 1
n = arr[m+1]
print(n)

# Number of passengers at end stop
bus_stops = [[10,0],[3,5],[5,8]]
sum([i - o for i, o in bus_stops])

# Membership classification
data = [[45, 12],[55,21],[19, -2],[104, 20]]
['Senior' if age >= 55 and handicap > 7 else 'Open' for (age, handicap) in data]

# Missing letter in alphabetic sequence
chars = ['K', 'L', 'M', 'O']
n = 0
while ord(chars[n]) == ord(chars[n+1]) + 1:
	n += 1
chr(1 + ord(chars[n]))

