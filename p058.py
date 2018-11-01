from euler_helpers import is_prime


def diagonals():
    diagonal = 1
    step = 2
    while True:
        for _ in range(4):
            diagonal += step
            yield diagonal
        step += 2


def p058():
    total = 1
    primes = 0
    length = 1
    ds = diagonals()
    while primes / total >= 0.1 or primes == 0:
        length += 2
        for _ in range(4):
            total += 1
            if is_prime(next(ds)):
                primes += 1
    print(length)


if __name__ == '__main__':
    p058()
