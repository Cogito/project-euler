from p035 import *


def test_circulate():
    circle1 = circulate(1)
    assert next(circle1) == 1
    assert next(circle1, None) is None
    circle2 = circulate(12)
    assert next(circle2) == 12
    assert next(circle2) == 21
    assert next(circle2, None) is None
