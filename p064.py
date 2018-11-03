from sympy.ntheory.continued_fraction import continued_fraction_periodic
import itertools
from tqdm import tqdm


def number_odd_period(N):
    total = 0
    for n in tqdm(range(1, N + 1)):
        continued_fraction = continued_fraction_periodic(0, 1, n)
        if len(continued_fraction) > 1 and len(continued_fraction[1]) % 2 == 1:
            total += 1
    return total


def p064():
    return number_odd_period(10000)


def test_p064():
    assert continued_fraction_periodic(0, 1, 23) == [4, [1, 3, 1, 8]]
    assert number_odd_period(13) == 4


if __name__ == '__main__':
    print(p064())
