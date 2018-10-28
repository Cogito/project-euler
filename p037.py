from euler_helpers import is_prime
from euler_helpers import primes


def left_truncated(number):
    number = str(number)
    while len(number) > 0:
        yield int(number)
        number = number[1:]


def right_truncated(number):
    number = str(number)
    while len(number) > 0:
        yield int(number)
        number = number[:-1]


def left_truncatable_prime(p):
    return all(is_prime(n) for n in left_truncated(p))


def right_truncatable_prime(p):
    return all(is_prime(n) for n in right_truncated(p))


def test_p037():
    right_truncated1 = right_truncated(1)
    assert next(right_truncated1) == 1
    assert next(right_truncated1, None) is None
    right_truncated2 = right_truncated(12)
    assert next(right_truncated2) == 12
    assert next(right_truncated2) == 1
    assert next(right_truncated2, None) is None
    left_truncated1 = left_truncated(1)
    assert next(left_truncated1) == 1
    assert next(left_truncated1, None) is None
    left_truncated2 = left_truncated(12)
    assert next(left_truncated2) == 12
    assert next(left_truncated2) == 2
    assert next(left_truncated2, None) is None

    assert left_truncatable_prime(3797)
    assert right_truncatable_prime(3797)


interesting_primes = []

for p in primes():
    if p < 10:
        continue
    if left_truncatable_prime(p) and right_truncatable_prime(p):
        interesting_primes.append(p)
    if len(interesting_primes) == 11:
        break

print(interesting_primes)
print(sum(interesting_primes))
