"""Tests for program 24: count vowels."""

import pytest
from codes.program_24_count_vowels import count_vowels


def test_case_1():
    assert count_vowels('hello') == 2


def test_case_2():
    assert count_vowels('AEIOU') == 5


def test_case_3():
    assert count_vowels('rhythm') == 0


def test_case_4():
    assert count_vowels('') == 0


def test_case_5():
    assert count_vowels('Python CI Pipeline') == 6

