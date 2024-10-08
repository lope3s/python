from unittest import TestCase
from main2 import has_not_overlapping_double_twin_letters, has_single_spread_twin_letters, string_matcher

class TestNotOverlappingDoubleTwinLetters(TestCase):
    def test_not_overlapping_double_twins(self):
        input = 'xyxyxyasdfuiopuy'
        output = has_not_overlapping_double_twin_letters(input)
        self.assertTrue(output)

    def test_not_overlapping_double_twins_spreaded(self):
        input = 'aabcdefgaafdsaio'
        output = has_not_overlapping_double_twin_letters(input)
        self.assertTrue(output)

    def test_overlapping_double_twins(self):
        input = 'aaaksdfqweruiopm'
        output = has_not_overlapping_double_twin_letters(input)
        self.assertFalse(output)

    def test_asdf(self):
        input = 'avccmveveqwhnjdx'
        output = has_not_overlapping_double_twin_letters(input)
        self.assertTrue(output)

class TestSingleSpreadTwinLetters(TestCase):
    def test_contains_repeated_letter_with_single_separator(self):
        input = 'xyx'
        output = has_single_spread_twin_letters(input)
        self.assertTrue(output)

    def test_contains_repeated_letter_with_single_separator_same_letters(self):
        input = 'aaa'
        output = has_single_spread_twin_letters(input)
        self.assertTrue(output)

    def test_asdf(self):
        input = 'avccmveveqwhnjdx'
        output = has_single_spread_twin_letters(input)
        self.assertTrue(output)


class TestStringMatcher(TestCase):
    def test_nice_str(self):
        input = 'qjhvhtzxzqqjkmpb'
        output = string_matcher(input)
        self.assertTrue(output)

    def test_naughty_str_doesnt_have_single_spread_twin_letters(self):
        input = 'uurcxstgmygtbstg'
        output = string_matcher(input)
        self.assertFalse(output)

    def test_naughty_str_doesnt_have_not_overlapping_double_twin_letters(self):
        input = 'ieodomkazucvgmuy'
        output = string_matcher(input)
        self.assertFalse(output)
