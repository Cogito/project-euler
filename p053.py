from gmpy import comb
from tqdm import tqdm


def p053():
    sum = 0
    for n in tqdm(range(1, 101)):
        for r in range(1, n + 1):
            if(comb(n, r)) > 1000000:
                sum += 1
    print(sum)


if __name__ == '__main__':
    p053()
