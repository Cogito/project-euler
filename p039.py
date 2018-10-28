import math
import gmpy
from collections import defaultdict

solutions = defaultdict(list)
for a in range(1, 1000):
    for b in range(1, 1000):
        c2 = a ** 2 + b ** 2
        if gmpy.is_square(c2):
            c = int(math.sqrt(c2))
            solutions[a + b + c].append((a, b, c))

max = 0
maxp = None
for p in solutions:
    if p < 1000 and len(solutions[p]) > max:
        print(p, len(solutions[p]))
        max = len(solutions[p])
        maxp = p

print(maxp)
print(solutions[maxp])
print(list((s, solutions[s]) for s in solutions if len(solutions[s]) > 15 and s < 1000))
