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

import matplotlib.pyplot as plt

plt.plot(range(10))
plt.show()
