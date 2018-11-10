from tqdm import tqdm
from itertools import count

count_mem = {}


def count_ways_to_write(n, less_than):
    if (n, less_than) in count_mem:
        return count_mem[(n, less_than)]
    output = 0
    for m in range(1, min(n, less_than) + 1):
        output += count_ways_to_write(n - m, m)
    if output == 0:
        output += 1
    count_mem[(n, less_than)] = output
    return output


partition_mem = {0: 1}


def partition_p(n):
    if n < 0:
        return 0
    if n not in partition_mem:
        partition_mem[n] = sum(((-1) ** (k + 1))*(partition_p(n - k * (3 * k - 1) // 2) + partition_p(n - k * (3 * k + 1) // 2)) for k in range(1, n + 1))
    return partition_mem[n]


def test_p078():
    assert count_ways_to_write(5, 5) == 7
    assert partition_p(5) == 7
    print(partition_p(1000))


def p078():
    for n in tqdm(count(2)):
        if partition_p(n) % 1000000 == 0:
            return n


if __name__ == '__main__':
    print(p078())
