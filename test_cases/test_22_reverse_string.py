"""Tests for program 22: reverse string."""

import pytest
from codes.program_22_reverse_string import reverse_string


def test_case_1():
    assert reverse_string('hello') == 'olleh'


def test_case_2():
    assert reverse_string('') == ''


def test_case_3():
    assert reverse_string('a') == 'a'


def test_case_4():
    assert reverse_string('12345') == '54321'


def test_case_5():
    assert reverse_string('Python CI') == 'IC nohtyP'

