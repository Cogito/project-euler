from euler_helpers import pandigitals, printlist


def substring_divisibility(number):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    return all((number % 10 ** (9 - n) // 10 ** (6 - n)) % divisor == 0 for (n, divisor) in enumerate(divisors))


def test_p043():
    number = 1406357289
    assert substring_divisibility(number)


if __name__ == '__main__':
    print(sum(number for number in pandigitals(10) if substring_divisibility(number)))
