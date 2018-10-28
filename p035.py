from euler_helpers import is_prime


def circulate(n):
    """Return the list of numbers that are formed by cycling the digits of n"""
    digits = list(d for d in str(n))
    for cycle in range(1, len(digits) + 1):
        yield int("".join(digits))
        digits = digits[1:] + [digits[0]]


checked = {}
num = 0

for number in range(1, 1000001):
    if number in checked:
        continue
    circle = list(circulate(number))
    if all(is_prime(c) for c in circle):
        num += len(circle)
        for c in circle:
            checked[c] = True

checked = sorted(checked)
print(checked)
print(len(checked))
