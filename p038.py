from euler_helpers import is_pandigital


def concatenated_product(integer, number):
    return "".join(str(integer * n) for n in range(1, number + 1))


def test_p038():
    assert concatenated_product(192, 3) == "192384576"
    assert is_pandigital(concatenated_product(192, 3), 9)


for a in range(1, 987654321):
    for b in range (2, 10):
        product = concatenated_product(a, b)
        if is_pandigital(product, 9):
            print(product)
