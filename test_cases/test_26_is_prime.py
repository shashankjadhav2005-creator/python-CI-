"""Tests for program 26: is prime."""

import pytest
from codes.program_26_is_prime import is_prime


def test_case_1():
    assert is_prime(2) == True


def test_case_2():
    assert is_prime(17) == True


def test_case_3():
    assert is_prime(1) == False


def test_case_4():
    assert is_prime(0) == False


def test_case_5():
    assert is_prime(21) == False


def test_negative_is_not_prime():
    assert is_prime(-7) is False

