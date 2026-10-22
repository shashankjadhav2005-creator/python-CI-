"""Tests for program 28: second largest."""

import pytest
from codes.program_28_second_largest import second_largest


def test_case_1():
    assert second_largest([1, 3, 2]) == 2


def test_case_2():
    assert second_largest([10, 10, 9]) == 9


def test_case_3():
    assert second_largest([-5, -2, -8]) == -5


def test_case_4():
    assert second_largest([1, 2, 3, 4]) == 3


def test_case_5():
    assert second_largest([0, -1, 1]) == 0


def test_requires_two_unique_values():
    with pytest.raises(ValueError):
        second_largest([4, 4])

