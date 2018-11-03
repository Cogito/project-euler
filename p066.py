from sympy.solvers.diophantine import diop_DN


def minimal_x_DN(D):
    return min(x for (x, y) in diop_DN(D, 1))


def max_D_for_DN(n):
    return max(range(1, n + 1), key=minimal_x_DN)


def test_p066():
    assert max_D_for_DN(7) == 5


def p066():
    return max_D_for_DN(1000)


if __name__ == '__main__':
    print(p066())
