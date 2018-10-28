from itertools import combinations
from euler_helpers import printlist


def insert_digits(number, num_digits):
    length = len(str(number))
    combos = combinations(range(length), length - num_digits)
    output = []
    for digit in range(num_digits):
        output.append((['*' if i in combo else 1 for i in range(3)] for combo in combos))


def p051():
    length = 2
    # positions = itertools.permutations(integers(end=length), 2)

    # printlist(integers(end=length))
    # printlist(positions)
    combos = combinations(range(3), 1)
    printlist()


if __name__ == '__main__':
    p051()
