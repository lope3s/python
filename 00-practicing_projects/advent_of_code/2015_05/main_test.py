from unittest import TestCase
from main import vowel_matcher, twin_letter_matcher, forbidden_matcher, string_matcher

class TestVowelMathcer(TestCase):
    def test_match_only_one_vowel_occurence(self):
        input = 'aeiouaeiouaeioua'
        output = vowel_matcher(input)
        self.assertTrue(output)

    def test_match_vowels(self):
        input = 'aei'
        output = vowel_matcher(input)
        self.assertTrue(output)

    def test_match_repeated_vowels(self):
        input = 'aaa'
        output = vowel_matcher(input)
        self.assertTrue(output)

    def test_match_sparse_vowels(self):
        input = 'xazegov'
        output = vowel_matcher(input)
        self.assertTrue(output)

class TestTwinLetterMatcher(TestCase):
    def test_contains_twin_letter(self):
        input = 'xx'
        output = twin_letter_matcher(input)
        self.assertTrue(output)

    def test_contains_twin_letter_sparsed(self):
        input = 'abcdde'
        output = twin_letter_matcher(input)
        self.assertTrue(output)

class TestForbiddenMatcher(TestCase):
    def test_contain_ab_cd_pq_xy(self):
        input = 'haegwjzuvuyypxyu'
        output = forbidden_matcher(input)
        self.assertTrue(output)

class TestStringMatcher(TestCase):
    def test_ugknbfddgicrmopn(self):
        input = 'ugknbfddgicrmopn'
        output = string_matcher(input)
        self.assertTrue(output)

    def test_aaa(self):
        input = 'aaa'
        output = string_matcher(input)
        self.assertTrue(output)

    def test_jchzalrnumimnmhp(self):
        input = 'jchzalrnumimnmhp'
        output = string_matcher(input)
        self.assertFalse(output)

    def test_haegwjzuvuyypxyu(self):
        input = 'haegwjzuvuyypxyu'
        output = string_matcher(input)
        self.assertFalse(output)

    def test_dvszwmarrgswjxmb(self):
        input = 'dvszwmarrgswjxmb'
        output = string_matcher(input)
        self.assertFalse(output)
