from sympy import totient
from tqdm import tqdm


def p070():
    return min_permutated_totient_ratio(10 ** 7)


def min_permutated_totient_ratio(N):
    return min((n for n in tqdm(range(2, N + 1)) if sorted(str(n)) == sorted(str(totient(n)))), key=lambda n: n / totient(n))


if __name__ == '__main__':
    print(p070())
