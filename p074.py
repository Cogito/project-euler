import math
from tqdm import tqdm

chain_lengths = {
    145: 1,
    871: 2, 45361: 2,
    872: 2, 45362: 2,
    169: 3, 363601: 3, 1454: 3
}


def chain_length(n):
    if n not in chain_lengths.keys():
        if sum_factorial_digits(n) == n:
            chain_lengths[n] = 1
        else:
            chain_lengths[n] = 1 + chain_length(sum_factorial_digits(n))
    return chain_lengths[n]


digit_factorials = dict((str(n), math.factorial(n)) for n in range(10))


def sum_factorial_digits(n):
    return sum(digit_factorials[d] for d in str(n))


def test_p074():
    assert sum_factorial_digits(145) == 145
    assert chain_length(169) == 3
    assert chain_length(69) == 5


def p074():
    return len([n for n in tqdm(range(1, 10 ** 6)) if chain_length(n) == 60])


if __name__ == '__main__':
    print(p074())
