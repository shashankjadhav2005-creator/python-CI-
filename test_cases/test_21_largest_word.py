"""Tests for program 21: largest word."""

import pytest
from codes.program_21_largest_word import largest_word


def test_case_1():
    assert largest_word('Python is powerful') == 'powerful'


def test_case_2():
    assert largest_word('one three seven') == 'three'


def test_case_3():
    assert largest_word('') == ''


def test_case_4():
    assert largest_word('tiny') == 'tiny'


def test_case_5():
    assert largest_word('red blue') == 'blue'

