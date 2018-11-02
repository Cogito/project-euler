def p063():
    n_digits_n_power = []
    for a in range(1, 1000):
        for b in range(1, 1000):
            power = a ** b
            if len(str(power)) == b:
                n_digits_n_power.append(power)
            if len(str(power)) > b:
                break
    print(n_digits_n_power)
    return len(n_digits_n_power)


if __name__ == '__main__':
    print(p063())
