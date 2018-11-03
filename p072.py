from sympy import totient
from tqdm import tqdm


def number_reduced_proper_fractions(max_denominator):
    return sum(totient(d) for d in tqdm(range(2, max_denominator + 1)))


def test_p072():
    assert number_reduced_proper_fractions(8) == 21


def p072():
    return number_reduced_proper_fractions(10 ** 6)


if __name__ == '__main__':
    print(p072())
