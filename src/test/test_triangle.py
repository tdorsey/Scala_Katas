import pytest
from main.triangle import Triangle


@pytest.mark.parametrize("lengths,expected",[
    ([3,3,3], True),
    ([1,2,3], False)
])
def test_equilateral(lengths, expected):
    triangle = Triangle(*lengths)
    assert(triangle.is_equilateral() == expected)

def test_isosceles():
    pass
    #assert(triangle.is_isosceles())

@pytest.mark.parametrize("lengths,expected",[
    ([3,4,5], True),
    ([1,2,3], False)
])
def test_right(lengths, expected):
    triangle = Triangle(*lengths)
    assert(triangle.is_right() == expected)

def test_scalene():
    pass
    #assert(triangle.is_scalene())

def test_invalid_triangle():
    pass

def test_combination():
    return True

def test_integer_input():
    return True

def test_noninteger_input():
    return True