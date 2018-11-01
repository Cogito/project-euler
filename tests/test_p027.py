from p027 import num_quadratic_primes


def test_num_quadratic_primes():
    assert num_quadratic_primes(1, 41) == 40
    assert num_quadratic_primes(-79, 1601) == 80
    # assert num_quadratic_primes(-999, 61) == 1011

