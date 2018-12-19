import pytest
from main.triangle import Triangle
"""
[3, 3, 3],  # 1, Equilateral
[5, 5, 3]  # 2, Isosceles
[3, 4, 5],  # 3 Right
[2, 3, 4],  # 4 Scalene
[2, 3, 5]  # 5 Not a triangle. TODO: Could be colinear, check with customer to clarify
"""

@pytest.mark.parametrize("lengths,expected",[
        ([3, 3, 3], True),
        ([5,5,3] , False),
        ([5, 3, 5], False),
        ([3,4,5], False),
        ([2,3,4], False),
        ([2, 3, 5], False)
])
def test_equilateral(lengths, expected):
    triangle = Triangle(*lengths)
    assert(triangle.is_equilateral() == expected)

@pytest.mark.parametrize("lengths,expected",[
    ([3, 3, 3], False),
    ([5,5,3] , True),
    ([5, 3, 5], True),
    ([3,4,5], False),
    ([2,3,4], False),
    ([2, 3, 5], False)
])
def test_isosceles(lengths, expected):
    triangle = Triangle(*lengths)
    assert (triangle.is_isosceles() == expected)

@pytest.mark.parametrize("lengths,expected",[
    ([3, 3, 3], False),
    ([5,5,3] , False),
    ([5, 3, 3], False),
    ([3,4,5], True),
    ([2,3,4], False),
    ([2, 3, 5], False)
])
def test_right(lengths, expected):
    triangle = Triangle(*lengths)
    assert(triangle.is_right() == expected)

@pytest.mark.parametrize("lengths,expected",[
        ([3, 3, 3], False),
        ([5,5,3] , False),
        ([5, 3, 5], False),
        ([3,4,5], False),
        ([2,3,4], True),
        ([2, 3, 5], False)
])
def test_scalene(lengths, expected):
    triangle = Triangle(*lengths)
    assert (triangle.is_scalene() == expected)

@pytest.mark.parametrize("lengths,expected",[
    ([3, 3, 3], False),
        ([5,5,3] , False),
    ([5, 3, 5], False),

    ([3,4,5], False),
        ([2,3,4], False),
        ([2, 3, 5], True)
])
def test_invalid_triangle(lengths, expected):
    triangle = Triangle(*lengths)
    assert (triangle.is_valid() == expected)


def test_integer_input():
    return True

def test_noninteger_input():
    return True