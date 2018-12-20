import pytest
from main.triangle import Triangle

"""
[3, 3, 3],  # 1, Equilateral
[5, 5, 3]  # 2, Isosceles
[3, 4, 5],  # 3 Right
[2, 3, 4],  # 4 Scalene
[2, 3, 5]  # 5 Not a triangle. TODO: Could be colinear, check with customer to clarify
"""

equilateral_data = [
    ([3, 3, 3], True),
    ([5, 5, 3], False),
    ([5, 3, 5], False),
    ([3, 4, 5], False),
    ([2, 3, 4], False),
    ([2, 3, 5], False)
]

isosceles_data = [
    ([3, 3, 3], False),
    ([5, 5, 3], True),
    ([5, 3, 5], True),
    ([3, 4, 5], False),
    ([2, 3, 4], False),
    ([2, 3, 5], False)
]

right_data = [
        ([3, 3, 3], False),
        ([5, 5, 3], False),
        ([5, 3, 3], False),
        ([3, 4, 5], True),
        ([2, 3, 4], False),
        ([2, 3, 5], False)
    ]

scalene_data = [
    ([3, 3, 3], False),
    ([5, 5, 3], False),
    ([5, 3, 5], False),
    ([3, 4, 5], False),
    ([2, 3, 4], True),
    ([2, 3, 5], False)
]

invalid_triangle_data =  [
    ([3, 3, 3], True),
    ([5, 5, 3], True),
    ([5, 3, 5], True),

    ([3, 4, 5], True),
    ([2, 3, 4], True),
    ([2, 3, 5], False)
]

@pytest.fixture(scope='module', params=equilateral_data)
def equilateral_test_case(request):
    return request.param

@pytest.fixture(scope='module', params=isosceles_data)
def isosceles_test_case(request):
    return request.param

@pytest.fixture(scope='module', params=right_data)
def right_test_case(request):
    return request.param

@pytest.fixture(scope='module', params=scalene_data)
def scalene_test_case(request):
    return request.param

@pytest.fixture(scope='module', params=invalid_triangle_data)
def invalid_triangle_test_case(request):
    return request.param


def test_equilateral(equilateral_test_case):
    lengths, expected = equilateral_test_case
    triangle = Triangle(*lengths)
    assert (triangle.is_equilateral == expected)



def test_isosceles(isosceles_test_case):
    lengths, expected = isosceles_test_case
    triangle = Triangle(*lengths)
    assert (triangle.is_isosceles == expected)


def test_right(right_test_case):
    lengths, expected = right_test_case
    triangle = Triangle(*lengths)
    assert (triangle.is_right == expected)


def test_scalene(scalene_test_case):
    lengths, expected = scalene_test_case
    triangle = Triangle(*lengths)
    assert (triangle.is_scalene == expected)


def test_invalid_triangle(invalid_triangle_test_case):
    lengths, expected = invalid_triangle_test_case
    triangle = Triangle(*lengths)
    assert (triangle.is_valid() == expected)



def test_noninteger_input():
    return False
