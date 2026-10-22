"""Tests for program 27: fibonacci."""

import pytest
from codes.program_27_fibonacci import fibonacci


def test_case_1():
    assert fibonacci(0) == []


def test_case_2():
    assert fibonacci(1) == [0]


def test_case_3():
    assert fibonacci(2) == [0, 1]


def test_case_4():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_case_5():
    assert fibonacci(5) == [0, 1, 1, 2, 3]


def test_negative_fibonacci_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)

