from itertools import combinations, cycle, count
from euler_helpers import printlist, is_prime, primes
from tqdm import tqdm


def insert_digits(number, num_digits):
    length = len(str(number)) + num_digits
    output = []
    char_cyc = cycle(str(number))
    combos = combinations(range(length), num_digits)
    for combo in combos:
        output.append([int("".join([str(digit) if i in combo else next(char_cyc) for i in range(length)])) for digit in range(10)])
    return output


def replace_digits(number, positions):
    number_string = str(number)
    output = []
    for position in positions:
        output.append([int("".join([str(digit) if i in position else number_string[i] for i in range(len(number_string))])) for digit in range(10)])
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


def p051():
    for number in tqdm(primes()):
        for family in replace_digits(number, find_doubles(number)):
            if sum(1 if is_prime(n) else 0 for n in family) >= 7:
                print([1 if is_prime(n) else 0 for n in family])
                print(family)
                if sum(1 if is_prime(n) else 0 for n in family) >= 8:
                    return


if __name__ == '__main__':
    p051()
    # printlist(list(d) for d in replace_digits(1234515812, find_doubles(1234515812)))
