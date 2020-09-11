#!/usr/bin/env python3

"""
This is the test code for the utils class
"""

import unittest
import utils

__author__ = "Alex DeCesare"
__version__ = "09-September-2020"

class TestIsValid(unittest.TestCase):

    def test_card_number_empty_string(self):

        is_number_valid = utils.is_valid('')

        self.assertFalse(is_number_valid)

    def test_card_number_length_well_below_minimum(self):

        is_number_valid = utils.is_valid('123')

        self.assertFalse(is_number_valid)

    def test_card_number_length_one_below_minimum(self):
        
        is_number_valid = utils.is_valid('123456789012')

        self.assertFalse(is_number_valid)

    def test_card_number_length_at_minimum(self):

        is_number_valid = utils.is_valid('1234567890123')

        self.assertTrue(is_number_valid)

    def test_card_number_length_one_above_minimum(self):

        is_number_valid = utils.is_valid('12345678901234')

        self.assertTrue(is_number_valid)

    def test_card_number_length_between_minimum_and_maximum(self):

        is_number_valid = utils.is_valid('1234567890123456')

        self.assertTrue(is_number_valid)

    def test_card_number_length_one_below_maximum(self):

        is_number_valid = utils.is_valid('123456789012345678')

        self.assertTrue(is_number_valid)

    def test_card_number_length_at_maximum(self):

        is_number_valid = utils.is_valid('1234567890123456789')

        self.assertTrue(is_number_valid)
        
    def test_card_number_length_one_above_maximum(self):

        is_number_valid = utils.is_valid('12345678912345678912')

        self.assertFalse(is_number_valid)

    def test_card_number_length_well_above_maximum(self):

        is_number_valid = utils.is_valid('123456789123456789123456789')

        self.assertFalse(is_number_valid)

    def test_card_number_only_letters(self):

        is_number_valid = utils.is_valid('not valid')

        self.assertFalse(is_number_valid)

    def test_card_number_letters_and_numbers(self):

        is_number_valid = utils.is_valid('78d68794d6g4545d')

        self.assertFalse(is_number_valid)

    def test_wrongly_grouped_card_number_by_space(self):

        is_number_valid = utils.is_valid('78 98 98 78 98 45 89 45')

        self.assertFalse(is_number_valid)

    def test_correctly_grouped_card_number_by_space(self):

        is_number_valid = utils.is_valid('7894 7894 5678 5478')

        self.assertTrue(is_number_valid)

    def test_wrongly_grouped_card_number_by_dash(self):

        is_number_valid = utils.is_valid('87-78-78-45-78-89-45-56')

        self.assertFalse(is_number_valid)

    def test_correctly_grouped_card_number_by_dash(self):

        is_number_valid = utils.is_valid('7845-7889-4556-7854')

        self.assertTrue(is_number_valid)

