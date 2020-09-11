#!/usr/bin/env python3

"""
This class contains the methods resposible for determining a valid credit card number
"""

import re

__author__ = "Alex DeCesare"
__version__ = "07-September-2020"

minimum_card_length = 13
four_digit_subgroup_card_length = 16
maximum_card_length = 19

def is_valid(sequence):

    """
    This function determines if a number sequence is a valid credit card number
    """

    card_digits_regex = re.compile(r'^[0-9-\s]+$')
    card_digits_match = card_digits_regex.search(sequence)

    if card_digits_match is not None:
        card_digits_group = card_digits_match.group()
        print(card_digits_group)

        if (len(card_digits_group) < minimum_card_length or len(card_digits_group) > maximum_card_length):
            return False

        if (len(card_digits_group) == four_digit_subgroup_card_length):
            four_digit_group_regex = re.compile(r'^(\d{4})+(-|\s)?(\d{4})+(-|\s)?(\d{4})+(-|\s)?(\d{4})$')
            four_digit_group_match = four_digit_group_regex.search(sequence)
            return True 

        return True

    else:
        return False

"""
def luhn_verified(credit_card_number):
"""
