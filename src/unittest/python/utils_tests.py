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

