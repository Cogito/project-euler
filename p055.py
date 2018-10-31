def is_Lychrel(n):
    test = n + int("".join(reversed(str(n))))
    for iteration in range(51):
        if is_palindrome(test):
            return False
        else:
            test = test + int("".join(reversed(str(test))))
    return True


def is_palindrome(n):
    return str(n) == "".join(reversed(str(n)))


def test_p055():
    assert 349 + int("".join(reversed(str(349)))) == 1292
    assert is_Lychrel(349)


def p055():
    print(sum(1 if is_Lychrel(n) else 0 for n in range(1, 10000)))


if __name__ == '__main__':
    p055()
