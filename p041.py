from euler_helpers import primes, is_pandigital

for p in primes():
    if p > 1000000000:
        break
    if is_pandigital(p):
        print(p)
