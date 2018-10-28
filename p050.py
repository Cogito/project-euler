import gmpy

consecutives = []
first_prime = 1

while first_prime < 10 ** 6:
    first_prime = gmpy.next_prime(first_prime)
    sum_primes = first_prime
    num_consecutive = 1
    next_p = first_prime
    while sum_primes < 10 ** 6:
        if num_consecutive > 1 and gmpy.is_prime(sum_primes):
            consecutives.append((num_consecutive, sum_primes))
        next_p = gmpy.next_prime(next_p)
        sum_primes += next_p
        num_consecutive += 1

print(sorted(consecutives))
