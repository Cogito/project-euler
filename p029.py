def power_sequence(x, y):
    return sorted(set(a ** b for a in range(x, y + 1) for b in range(x, y + 1)))


print(len(power_sequence(2, 100)))
