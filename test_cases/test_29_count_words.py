"""Tests for program 29: count words."""

import pytest
from codes.program_29_count_words import count_words


def test_case_1():
    assert count_words('hello world') == 2


def test_case_2():
    assert count_words('') == 0


def test_case_3():
    assert count_words('  one   two  three ') == 3


def test_case_4():
    assert count_words('single') == 1


def test_case_5():
    assert count_words('Python CI pipeline tests') == 4

