from itertools import combinations, cycle, count
from euler_helpers import printlist, is_prime, primes
from tqdm import tqdm
from collections import Counter


def insert_digits(number, num_digits):
    length = len(str(number)) + num_digits
    output = []
    char_cyc = cycle(str(number))
    combos = combinations(range(length), num_digits)
    for combo in combos:
        for digit in range(10):
            if 0 in combo and digit == 0:
                continue
            output.append([int("".join([str(digit) if i in combo else next(char_cyc) for i in range(length)]))])
    return output


def replace_digits(number, positions):
    number_string = str(number)
    output = []
    for position in positions:
        family = []
        for digit in range(10):
            if 0 in position and digit == 0:
                continue
            family.append([int("".join([str(digit) if i in position else number_string[i] for i in range(len(number_string))]))])
            print(family)
        output.append(family)
    return output


def find_doubles(number):
    locations = [[], [], []]
    for i, c in enumerate(str(number)):
        if c == '0':
            locations[0].append(i)
        if c == '1':
            locations[1].append(i)
        if c == '2':
            locations[2].append(i)
    doubles = []
    for l in locations:
        if len(l) >= 2:
            doubles.extend(combinations(l, 2))
    return doubles


def find_triples(number):
    locations = [[], [], [], []]
    for i, c in enumerate(str(number)):
        if c == '0':
            locations[0].append(i)
        if c == '1':
            locations[1].append(i)
        if c == '2':
            locations[2].append(i)
    triples = []
    for l in locations:
        if len(l) >= 3:
            triples.extend(combinations(l, 3))
    return triples


def find_repeats(number):
    locations = [[] for _ in range(10)]
    repeats = []
    for i, c in enumerate(str(number)):
        locations[int(c)].append(i)
    for num_digits in range(2, len(str(number)) + 1):
        for l in locations:
            if len(l) >= num_digits:
                repeats.extend(combinations(l, num_digits))
    return repeats


def p051():
    for number in tqdm(primes()):
        for family in replace_digits(number, find_repeats(number)):
    # for number in tqdm(count(start=10)):
    #     for num_digits in range(1, 3):
    #         # num_digits = 1
    #         for family in insert_digits(number, num_digits):
                if sum(1 if is_prime(n) else 0 for n in family) >= 7:
                    print(number)
                    print(sum(1 if is_prime(n) else 0 for n in family), [1 if is_prime(n) else 0 for n in family])
                    print(family)
                    if sum(1 if is_prime(n) else 0 for n in family) >= 8:
                        return


if __name__ == '__main__':
    # printlist(p for p in [2090021, 2191121, 2292221, 2393321, 2494421, 2595521, 2696621, 2797721, 2898821, 2999921] if is_prime(p))
    p051()
    # printlist(list(d) for d in replace_digits(1234515812, find_repeats(1234515812)))
    # printlist(insert_digits(13,1))
