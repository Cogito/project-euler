from tqdm import tqdm
from primesieve import primes
from itertools import count

count_mem = {}


def count_as_sums_of_primes(n, less_than):
    if (n, less_than) in count_mem:
        return count_mem[(n, less_than)]
    output = 0
    for m in primes(min(n, less_than)):
        output += count_as_sums_of_primes(n - m, m)
    if n == 0:
        output += 1
    count_mem[(n, less_than)] = output
    return output


def test_p077():
    assert count_as_sums_of_primes(10, 9) == 5


def p077():
    for n in tqdm(count(2)):
        if count_as_sums_of_primes(n, n - 1) > 5000:
            return n


if __name__ == '__main__':
    print(p077())
