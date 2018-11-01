import itertools
from lib_primes import is_prime


def quadratic(a, b):
    n = 0
    while True:
        yield n ** 2 + a * n + b
        n += 1


def quadratic_primes(a, b):
    q = quadratic(a, b)
    return itertools.takewhile(is_prime, q)


def num_quadratic_primes(a, b):
    n = 0
    q = quadratic(a, b)
    while is_prime(next(q)):
        n += 1
    return n


largest = dict(
    a=1,
    b=41,
    n_primes=40
)

for x in range(1000, -1000, -1):
    for y in range(1001, -1001, -1):
        n_primes = num_quadratic_primes(x, y)
        if n_primes > largest['n_primes']:
            print(dict(a=x, b=y, n_primes=n_primes))
            largest = dict(a=x, b=y, n_primes=n_primes)

print(largest)
print(largest['a'] * largest['b'])
print(list((p, is_prime(p)) for p in quadratic_primes(largest['a'], largest['b'])))
