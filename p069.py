from sympy import totient


def p069():
    return max_totient_ratio(1000000)


def max_totient_ratio(N):
    return max((n for n in range(2, N + 1)), key=lambda n: n / totient(n))


def test_p069():
    assert max_totient_ratio(10) == 6


if __name__ == '__main__':
    print(p069())
