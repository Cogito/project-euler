from gmpy import gcd
from tqdm import tqdm


def find_rpf_less_than(max_denominator, fraction):
    greatest = 0
    rpf = (0, 1)
    for denominator in tqdm(range(1, max_denominator + 1)):
        numerator = int(denominator * fraction)
        ratio = numerator / denominator
        if greatest < ratio < 3 / 7 and gcd(numerator, denominator) == 1:
            greatest = ratio
            rpf = (numerator, denominator)
    return rpf


def test_p071():
    assert find_rpf_less_than(8, 3 / 7) == (2, 5)


def p071():
    return find_rpf_less_than(10 ** 6, 3 / 7)[0]


if __name__ == '__main__':
    print(p071())
