def p056():
    print(max(digit_sum(a ** b) for a in range(1, 100) for b in range(1, 100)))


def digit_sum(n):
    return sum(int(digit) for digit in str(n))


if __name__ == '__main__':
    p056()
