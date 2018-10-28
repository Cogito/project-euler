def pentagonal(n):
    return n * (3 * n - 1) / 2


def test_difference(n=3):
    difference = pentagonal(n) - pentagonal(n - 1)
    assert difference == (3 / 2 * n ** 2 - 1 / 2 * n) - (3 / 2 * (n - 1) ** 2 - 1 / 2 * (n - 1))
    assert difference == (3 / 2 * n ** 2 - 1 / 2 * n) - (3 / 2 * (n ** 2 - 2 * n + 1) - 1 / 2 * (n - 1))
    assert difference == (3 / 2 * n ** 2 - 1 / 2 * n) - (3 / 2 * n ** 2 - 1 / 2 * n + 3 / 2 * (- 2 * n + 1) + 1 / 2)
    assert difference == (3 / 2 * n ** 2 - 1 / 2 * n) - (3 / 2 * n ** 2 - 1 / 2 * n) - (-3 * n + 3 / 2 + 1 / 2)
    assert difference == 3 * n - 2


pentagonals = []

for n in range(1, 10 ** 4):
    new_pentagonal = pentagonal(n)
    if n % 10 ** 3 == 0:
        print(new_pentagonal)
    for a in pentagonals:
        for b in pentagonals:
            if a + b > new_pentagonal:
                break
            if a + b == new_pentagonal and abs(a - b) in pentagonals:
                print(a, b, new_pentagonal, a - b, (a - b) in pentagonals)

    pentagonals.append(new_pentagonal)
