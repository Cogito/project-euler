from itertools import combinations, cycle, count
from euler_helpers import printlist, is_prime


def insert_digits(number, num_digits):
    length = len(str(number)) + num_digits
    output = []
    char_cyc = cycle(str(number))
    combos = combinations(range(length), num_digits)
    for combo in combos:
        output.append([int("".join([str(digit) if i in combo else next(char_cyc) for i in range(length)])) for digit in range(10)])
    return output


def p051():
    for number in count():
        for family in insert_digits(number, 2):
            if sum(1 if is_prime(n) else 0 for n in family) >= 8:
                print([1 if is_prime(n) else 0 for n in family])
                print(family)
                return


if __name__ == '__main__':
    p051()
