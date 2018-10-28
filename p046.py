from euler_helpers import primes, is_prime
import gmpy
from tqdm import tqdm


def test_p046():
    assert is_goldbach(33)


def is_goldbach(n):
    for p in primes():
        if p > n:
            return False
        if (n - p) % 2 != 0:
            continue
        sub_p = (n - p) // 2
        if gmpy.is_square(sub_p):
            if (n % 1000 == 1):
                print(f'{n} = {p} + 2*{sub_p}')
            return True
    return False


def first_non_goldbach():
    for composite in tqdm(range(33, 10 ** 5, 2)):
        if is_prime(composite):
            continue
        if not is_goldbach(composite):
            return composite


if __name__ == '__main__':
    print(first_non_goldbach())
