"""Tests for program 30: character frequency."""

import pytest
from codes.program_30_character_frequency import character_frequency


def test_case_1():
    assert character_frequency('aba') == {'a': 2, 'b': 1}


def test_case_2():
    assert character_frequency('') == {}


def test_case_3():
    assert character_frequency('Aa') == {'A': 1, 'a': 1}


def test_case_4():
    assert character_frequency('hello') == {'h': 1, 'e': 1, 'l': 2, 'o': 1}


def test_case_5():
    assert character_frequency('a a') == {'a': 2, ' ': 1}

