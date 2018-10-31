from p032 import *


def test_pandigital():
    assert pandigital(str(39) + str(186) + str(7254))


def test_unusual_pandigital():
    assert unusual_pandigital(39, 186, 7254)
