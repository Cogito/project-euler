import itertools
from euler_helpers import is_prime, primes
from tqdm import tqdm


def concatenate_numbers(numbers):
    return (int(f'{a}{b}') for a, b in (p for p in itertools.permutations(numbers, 2)))


def concatenating_primes(numbers):
    return all(is_prime(p) for p in concatenate_numbers(numbers))


def test_p060():
    assert all(is_prime(p) for p in concatenate_numbers([3, 7, 109, 673]))
    assert concatenating_primes([3, 7, 109, 673])


def p060():
    familys = []
    for p in tqdm(primes()):
        for family in familys:
            candidate = [*family, p]
            if all(is_prime(int(f'{p}{f}')) and is_prime(int(f'{f}{p}')) for f in family):
                if len(candidate) >= 4:
                    print(f'length:{len(candidate)}, sum:{sum(candidate):20}', candidate)
                if len(candidate) >= 5:
                    return
                familys.append(candidate)
        familys.append([p])


if __name__ == '__main__':
    p060()
