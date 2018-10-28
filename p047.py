from euler_helpers import prime_factors
from tqdm import tqdm


def num_distinct_factors(n):
    return len(prime_factors(n))


def all_integers(start=1):
    while True:
        yield start
        start += 1


def test_p047():
    assert num_distinct_factors(644) == num_distinct_factors(645) == num_distinct_factors(646) == 3
    assert first_consecutive_with_distinct_factors(2, 2)[0] == 14
    assert first_consecutive_with_distinct_factors(3, 3)[0] == 644


def first_consecutive_with_distinct_factors(num_consecutive, num_factors, start=1):
    num_found = 0
    for test in tqdm(all_integers(start)):
        if num_distinct_factors(test) == num_factors:
            num_found += 1
            if num_found == num_consecutive:
                print(test, num_consecutive, num_factors)
                return list(range(test - num_consecutive + 1, test + 1))
            if num_found == num_consecutive - 1:
                print(test, num_consecutive, num_factors, num_found)
        else:
            num_found = 0


if __name__ == '__main__':
    print(first_consecutive_with_distinct_factors(4, 4, 10000))
