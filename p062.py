import itertools
import sympy
import collections
from tqdm import tqdm
from euler_helpers import digit_sum

cubes_mem = [n ** 3 for n in range(10 ** 5)]


def cubes():
    yield from (n ** 3 for n in itertools.count(start=1))


def is_perfect_cube(x):
    return sympy.integer_nthroot(x, 3)[1]


def digit_product(n):
    """Return the product of the non-zero digits"""
    p = 1
    for i in str(n):
        if int(i) != 0:
            p *= int(i)
    return p


def permutations_of_each_other(numbers):
    ordered = [sorted(str(n)) for n in numbers]
    return all(n == ordered[0] for n in ordered)


def p062():
    buckets = collections.defaultdict(list)
    for cube in tqdm(cubes_mem):
        buckets[(len(str(cube)), digit_sum(cube), digit_product(cube))].append(cube)
    for key, bucket in buckets.items():
        if len(bucket) >= 5:
            for set_of_5 in itertools.combinations(bucket, 5):
                if permutations_of_each_other(set_of_5):
                    return set_of_5


def test_p062():
    assert is_perfect_cube(27)
    assert not is_perfect_cube(10)
    assert is_perfect_cube(345 ** 3)


if __name__ == '__main__':
    print(p062())
