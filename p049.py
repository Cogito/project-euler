from euler_helpers import is_prime, primes, pairs, int_permutations
import itertools


def is_arithmetic_series(series):
    ratio = None
    for a, b in pairs(sorted(series)):
        if ratio is None:
            ratio = b - a
            if ratio == 0:
                return False
        else:
            if b - a != ratio:
                return False
    return True


def test_p049():
    assert is_prime(1487) and is_prime(4817) and is_prime(8147)
    assert is_arithmetic_series([1487, 4817, 8147])
    assert not is_arithmetic_series([1487, 4817, 7841])
    assert not is_arithmetic_series([1487, 4817, 1])


def first_four_digit_series():
    for p in primes():
        if p < 1000:
            continue
        if p > 9999:
            break
        for series in itertools.permutations(sorted(int_permutations(p)), 3):
            # if is_arithmetic_series(series):
            #     print(series)
            if 1487 not in series and is_arithmetic_series(series) and all(s > 1000 and is_prime(s) for s in series):
                print(series)
                return series


if __name__ == '__main__':
    # print("".join(first_four_digit_series()))
    print(first_four_digit_series())
