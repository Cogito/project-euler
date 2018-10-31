from fractions import Fraction as F


def root2_continued(iterations):
    results = []
    prev_value = 1
    for _ in range(iterations):
        value = prev_value = F(1) + F(1, 1 + prev_value)
        results.append(value)
    return results


def p057():
    print(sum(1 if len(str(fraction.numerator)) > len(str(fraction.denominator)) else 0 for fraction in root2_continued(1000)))


if __name__ == '__main__':
    p057()
