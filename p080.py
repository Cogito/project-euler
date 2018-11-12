import decimal
from euler_helpers import digit_sum


def square_root_digits(n, num_digits):
    decimal.getcontext().prec = num_digits+10
    return str(decimal.Decimal(n).sqrt())[:num_digits+1]


def sum_digits_if_not_square(n, num_digits):
    digits = square_root_digits(n, num_digits)
    return digits if '.' in digits else 0


def test_p080():
    assert digit_sum(sum_digits_if_not_square(2, 100)) == 475
    assert digit_sum(sum_digits_if_not_square(4, 100)) == 0


def p080():
    for n in range(1, 101):
        print(f'{n}: {digit_sum(sum_digits_if_not_square(n, 100))}, {sum_digits_if_not_square(n, 100)}')
    return sum(digit_sum(sum_digits_if_not_square(n, 100)) for n in range(1, 101))


if __name__ == '__main__':
    print(p080())

