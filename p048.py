def self_powers(number):
    return sum(n ** n for n in range(1, number + 1))


def test_self_powers():
    assert self_powers(10) == 10405071317


print(str(self_powers(1000))[-10:])
