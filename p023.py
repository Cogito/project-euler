import itertools


def is_abundant(n):
    return sum_factors(n) - n > n


def sum_factors(n):
    return sum(factors(n))


def factors(n):
    step = 2 if n % 2 else 1
    return set(itertools.chain(*([i, n // i] for i in range(1, int(n ** 0.5) + 1) if not n % i)))


abundant_numbers = list(n for n in range(1, 28123 - 12) if is_abundant(n))
sum_of_abundants = list(a + b for [a, b] in itertools.product(abundant_numbers, abundant_numbers))
not_in_abundants = list(n for n in range(1, 28123) if n not in sum_of_abundants)
print(sum(not_in_abundants))
print(list(not_in_abundants))
