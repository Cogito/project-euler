import primesieve
import itertools
import gmpy


def is_prime(n):
    """Returns True if n is prime."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def primes():
    it = primesieve.Iterator()
    while True:
        yield it.next_prime()


def prime_factors(x):
    prime = gmpy.mpz(2)
    x = gmpy.mpz(x)
    factors = {}
    while x >= prime:
        newx, mult = x.remove(prime)
        if mult:
            factors[prime] = mult
            x = newx
        prime = prime.next_prime()
    return factors


def pairs(seq):
    i = iter(seq)
    prev = next(i, None)
    for item in i:
        yield prev, item
        prev = item


def is_pandigital(number, length=None):
    number = str(number)
    if length and len(number) != length:
        return False
    if len(number) > 9:
        return False
    return all(number.count(str(d)) == 1 for d in range(1, len(number) + 1))


def pandigitals(length=10):
    for digits in itertools.permutations('1234567890'[:length]):
        yield int("".join(digits))


def printlist(iter):
    print(list(iter))


def test_pandigital():
    assert is_pandigital(1)
    assert is_pandigital(12)
    assert is_pandigital(987654321)
    assert not is_pandigital(13579)


def int_permutations(integer):
    for digits in itertools.permutations(str(integer)):
        yield int("".join(digits))


def triangle_numbers(minimum=0, maximum=float('inf')):
    numbers = (n * (n + 1) // 2 for n in itertools.count(start=1))
    yield from (n for n in itertools.takewhile(lambda n: n <= maximum, numbers) if minimum <= n)


def square_numbers(minimum=0, maximum=float('inf')):
    numbers = (n ** 2 for n in itertools.count(start=1))
    yield from (n for n in itertools.takewhile(lambda n: n <= maximum, numbers) if minimum <= n)


def pentagonal_numbers(minimum=0, maximum=float('inf')):
    numbers = (n * (3 * n - 1) // 2 for n in itertools.count(start=1))
    yield from (n for n in itertools.takewhile(lambda n: n <= maximum, numbers) if minimum <= n)


def hexagonal_numbers(minimum=0, maximum=float('inf')):
    numbers = (n * (2 * n - 1) for n in itertools.count(start=1))
    yield from (n for n in itertools.takewhile(lambda n: n <= maximum, numbers) if minimum <= n)


def heptagonal_numbers(minimum=0, maximum=float('inf')):
    numbers = (n * (5 * n - 3) // 2 for n in itertools.count(start=1))
    yield from (n for n in itertools.takewhile(lambda n: n <= maximum, numbers) if minimum <= n)


def octagonal_numbers(minimum=0, maximum=float('inf')):
    numbers = (n * (3 * n - 2) for n in itertools.count(start=1))
    yield from (n for n in itertools.takewhile(lambda n: n <= maximum, numbers) if minimum <= n)


def digit_sum(n):
    return sum(int(digit) for digit in str(n) if digit.isdigit())


def digit_product(n):
    p = 1
    for i in str(n):
        p *= int(i)
    return p
