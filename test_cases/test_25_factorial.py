"""Tests for program 25: factorial."""

import pytest
from codes.program_25_factorial import factorial


def test_case_1():
    assert factorial(0) == 1


def test_case_2():
    assert factorial(1) == 1


def test_case_3():
    assert factorial(5) == 120


def test_case_4():
    assert factorial(7) == 5040


def test_case_5():
    assert factorial(10) == 3628800


def test_negative_factorial_raises():
    with pytest.raises(ValueError):
        factorial(-1)

