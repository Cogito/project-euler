def step(x, y, size):
    right = down = final = 0
    if x < size:
        right = step(x+1, y, size)
    if y < size:
        down = step(x, y+1, size)
    if x == size and y == size:
        final = 1
    return right + down + final


def routes(size):
    return step(0, 0, size)


print(routes(12))
