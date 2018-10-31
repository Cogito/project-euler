import itertools


def pandigital(string):
    if len(string) != 9:
        return False
    for n in "123456789":
        if str.count(string, n) != 1:
            return False
    return True


def unusual_pandigital(multiplicand, multiplier, product):
    return multiplicand * multiplier == product and pandigital(str(multiplicand) + str(multiplier) + str(product))


def generate_unusual_pandigital():
    digits = "123456789"
    for length1 in range(1, 5):
        # print(length1)
        for length2 in range(1, 5):
            for string1 in itertools.permutations(digits, length1):
                # print(str.join("", string1))
                multiplicand = int(str.join("", string1))
                for string2 in itertools.permutations(digits.strip(str.join("", string1)), length2):
                    multiplier = int(str.join("", string2))
                    if multiplier > multiplicand and unusual_pandigital(multiplicand, multiplier, multiplicand * multiplier):
                        yield (multiplicand, multiplier, multiplicand * multiplier)


unusual_pandigitals = list(generate_unusual_pandigital())
print(unusual_pandigitals)
print(sum(set(product for (_, _, product) in unusual_pandigitals)))
