from sympy.ntheory.continued_fraction import continued_fraction_reduce
from sympy import fraction
from euler_helpers import digit_sum


def e_convergent_fraction(n):
    def cycle():
        k = 2
        yield 2
        while True:
            yield 1
            yield k
            yield 1
            k += 2

    c = cycle()
    for _ in range(n):
        yield next(c)


def p065():
    return digit_sum(fraction(continued_fraction_reduce(e_convergent_fraction(100)))[0])


def test_p065():
    assert digit_sum(fraction(continued_fraction_reduce([2, 1, 2, 1, 1, 4, 1, 1, 6, 1]))[0]) == 17
    assert digit_sum(fraction(continued_fraction_reduce(e_convergent_fraction(10)))[0]) == 17


if __name__ == '__main__':
    print(p065())
