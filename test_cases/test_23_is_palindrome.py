"""Tests for program 23: is palindrome."""

import pytest
from codes.program_23_is_palindrome import is_palindrome


def test_case_1():
    assert is_palindrome('level') == True


def test_case_2():
    assert is_palindrome('Python') == False


def test_case_3():
    assert is_palindrome('A man, a plan, a canal: Panama!') == True


def test_case_4():
    assert is_palindrome('') == True


def test_case_5():
    assert is_palindrome('Was it a car or a cat I saw?') == True

