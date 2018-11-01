import math

print(math.factorial(9) * 7)


def digits(n):
    return (int(c) for c in str(n))


def sum_factorial(n):
    return sum(math.factorial(d) for d in digits(n))


def curious_numbers():
    return (n for n in range(1, 10000000) if n == sum_factorial(n))


print(list(curious_numbers()))
