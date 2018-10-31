from collections import Counter
from itertools import count
from tqdm import tqdm


def p052():
    for n in tqdm(count(start=1)):
        digits = Counter(str(n))
        if all(Counter(str(n * multiple)) == digits for multiple in range(2, 7)):
            print(n)
            return


if __name__ == '__main__':
    p052()
