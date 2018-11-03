from gmpy import gcd
from tqdm import tqdm


def find_rpf_between(max_denominator, lo, hi):
    for denominator in tqdm(range(1, max_denominator + 1)):
        for numerator in range(int(denominator * lo), int(denominator * hi) + 1):
            ratio = numerator / denominator
            if lo < ratio < hi and gcd(numerator, denominator) == 1:
                yield (numerator, denominator)


def test_p073():
    assert len(list(find_rpf_between(8, 1 / 3, 1 / 2))) == 3


def p073():
    return len(list(find_rpf_between(12000, 1 / 3, 1 / 2)))


if __name__ == '__main__':
    print(p073())
