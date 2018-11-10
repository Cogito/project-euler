from tqdm import tqdm

mem = {}


def ways_to_write(n, less_than):
    if (n, less_than) in mem:
        return mem[(n, less_than)]
    output = []
    iterable = range(1, min(n, less_than) + 1)
    for m in tqdm(iterable) if n == 100 else iterable:
        for item in ways_to_write(n - m, m):
            output.append([m, *item])
    if len(output) == 0:
        output = [output]
    mem[(n, less_than)] = output
    return output


count_mem = {}


def count_ways_to_write(n, less_than):
    if (n, less_than) in count_mem:
        return count_mem[(n, less_than)]
    output = 0
    iterable = range(1, min(n, less_than) + 1)
    for m in tqdm(iterable) if n == 100 else iterable:
        output += count_ways_to_write(n - m, m)
    if output == 0:
        output += 1
    count_mem[(n, less_than)] = output
    return output


def test_p076():
    assert len(ways_to_write(5, 4)) == 6
    assert count_ways_to_write(5, 4) == 6


def p076():
    n = 100
    # return len(ways_to_write(n, n - 1))
    return count_ways_to_write(n, n - 1)


if __name__ == '__main__':
    print(p076())

# 1
#
# 1 1
#
# 2 1
# 1 1 1
#
# 3 1
# 2 2
# 2 1 1
# 1 1 1 1
#
# 4 1
# 3 2
# 3 1 1
# 2 2 1
# 2 1 1 1
# 1 1 1 1 1
#
# 5 1
# 4 2
# 4 1 1
# 3 3
# 3 2 1
# 3 1 1 1
# 2 2 2
# 2 2 1 1
# 2 1 1 1 1
# 1 1 1 1 1 1
#
# 6 1
# 5 2
# 5 1 1
# 4 3
# 4 2 1
# 4 1 1 1
# 3 4
