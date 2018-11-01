
primes = {}


def is_prime(n):
    """Returns True if n is prime."""
    result = None
    if n in primes:
        return primes[n]
    if n <= 0:
        result = False
    elif n == 2:
        result = True
    elif n == 3:
        result = True
    elif n % 2 == 0:
        result = False
    elif n % 3 == 0:
        result = False

    i = 5
    w = 2

    while result is None:
        if n % i == 0:
            result = False
        elif i * i > n:
            result = True
        i += w
        w = 6 - w

    primes[n] = result
    return result
