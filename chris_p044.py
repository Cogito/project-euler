# euler44

import itertools
import math
from tqdm import tqdm


def n_from_p(p):
    # Calculates n value from pentagonal number p
    # Returns none if p is not a pentagonal number

    sol = (1 + math.sqrt(1 + (24 * p))) / 6
    # sol2 = (1 - math.sqrt(1 + (24*p)))/2

    if sol.is_integer():
        return int(sol)
    else:
        return None


def p_from_n(n):
    return int(n * ((3 * n) - 1) / 2)


# Consider only the first 100 pentagonal numbers
final_range_val = 10001

print("Loading indices...")
# Generate indices
inds = list(itertools.combinations(range(1, final_range_val), 2))

# print(inds)

lowest = 10000000000000

print("Beginning test")
for ind in tqdm(inds):
    j = ind[0]
    p_j = p_from_n(j)
    k = ind[1]
    p_k = p_from_n(k)

    psum = p_j + p_k
    pdif = p_k - p_j

    # print("P_" + str(j) + " = " + str(p_j) + ", P_" + str(k) + " = " + str(p_k))
    # print("Sum = " + str(psum))
    # print("Difference = " + str(pdif))
    # input()

    if n_from_p(psum):
        # print(str(psum) + " is a penatagonal number too")

        if n_from_p(pdif):
            win = pdif
            # print("Found solution with " + str(p_j) + " and " + str(p_k) + ". D = " + str(pdif))
            if pdif < lowest:
                lowest = pdif

print("Result: " + str(lowest))
