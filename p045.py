from tqdm import tqdm


def pentagonals():
    n = 1
    while True:
        yield n * (3 * n - 1) / 2
        n += 1


def triangles():
    n = 1
    while True:
        yield n * (n + 1) / 2
        n += 1


def hexagonals():
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1


p = h = 1
ps = pentagonals()
hs = hexagonals()
ts = triangles()

for t in tqdm(ts):
    while p < t:
        p = next(ps)
    while h < t:
        h = next(hs)
    if t == p == h:
        print(t)
