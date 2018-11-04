from tqdm import tqdm
from collections import defaultdict


def triangle_mn(m, n):
    return sorted((m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2))


def triangles_mn_smaller_than(m, n, L):
    triangle = triangle_mn(m, n)
    return [list(n * e for e in triangle) for n in range(1, 1 + L // sum(triangle))]


def max_b(L, a):
    return 1 + int((L * (1 / 2 * L - a)) / (L - a))


def triangles_from_wire(L):
    count = defaultdict(int)
    triangles = set()
    for m in tqdm(range(2, 1 + int((L / 2) ** (1 / 2)))):  # Uses identity that m(m+n) <= L/2
        for n in range(1, min(m, 1 + int((L / 2 - m ** 2) / m))):
            for triangle in triangles_mn_smaller_than(m, n, L):
                triangles.add(tuple(triangle))
    for triangle in triangles:
        count[sum(triangle)] += 1
    return count


def count_only_1_triangle(L):
    return sum(1 if count == 1 else 0 for _, count in triangles_from_wire(L).items())


def p075():
    return count_only_1_triangle(1500000)


def test_p075():
    assert triangle_mn(2, 1) == [3, 4, 5]
    assert triangles_mn_smaller_than(2, 1, 12) == [[3, 4, 5]]
    assert triangles_mn_smaller_than(2, 1, 24) == [[3, 4, 5], [6, 8, 10]]
    assert count_only_1_triangle(12) == 1


if __name__ == '__main__':
    print(p075())
