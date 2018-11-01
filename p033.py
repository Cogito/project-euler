def product(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p


def fractions():
    for numerator in range(10, 100):
        for denominator in range(10, 100):
            if numerator != denominator and numerator % 10 != 0 and denominator % 10 != 0:
                yield (numerator, denominator, numerator / denominator)


def is_curious_fraction(fraction):
    numerator, denominator, f = fraction
    for digit in str(numerator):
        if digit in str(denominator) and int(str(numerator).replace(digit, "", 1)) / int(str(denominator).replace(digit, "", 1)) == f and f < 1:
            return True
    return False


curious_fractions = list(f for f in fractions() if is_curious_fraction(f))
print(curious_fractions)
print(product(f for (_, _, f) in curious_fractions))
