#!/usr/bin/env python3

"""
This class contains the methods resposible for determining a valid credit card number
"""

import re

__author__ = "Alex DeCesare"
__version__ = "07-September-2020"

MINIMUM_CARD_LENGTH = 13
FOUR_DIGIT_SUBGROUP_CARD_LENGTH = 16
MAXIMUM_CARD_LENGTH = 19
MAX_LUHN_ALGORITHM_DIGIT = 9
MULTIPLE_OF_TEN = 10

def is_valid(sequence):
    """
    This function determines if a number sequence is a valid credit card number
    """
    card_digits_regex = re.compile(r'^[0-9-\s]+$')
    card_digits_match = card_digits_regex.search(sequence)

    if card_digits_match is not None:
        card_digits_group = card_digits_match.group()
        card_length = len(card_digits_group)

        if card_length < MINIMUM_CARD_LENGTH or card_length > MAXIMUM_CARD_LENGTH:
            return False

        if len(card_digits_group) == FOUR_DIGIT_SUBGROUP_CARD_LENGTH:
            four_digit_group_string = r'^(\d{4})+(-|\s)?(\d{4})+(-|\s)?(\d{4})+(-|\s)?(\d{4})$'
            four_digit_group_regex = re.compile(four_digit_group_string)
            four_digit_group_regex.search(sequence)
            return True

        return True

    return False

def luhn_verified(credit_card_number):
    """
    This function uses the luhn algorithm to determine if a given credit card number is a fake or
    an authentic card number
    """

    credit_card_digits = credit_card_number.replace(' ', '').replace('-', '')
    dropped_last_digit = credit_card_digits[:len(credit_card_digits) - 1]
    last_card_digit = int(credit_card_digits[(len(credit_card_digits) - 1):len(credit_card_digits)])
    reverse_card_number = dropped_last_digit[::-1]

    total_checksum = 0
    index = 0

    while index < len(reverse_card_number):

        if index % 2 != 0:
            total_checksum += int(reverse_card_number[index])
        else:
            if (int(reverse_card_number[index]) * 2) > MAX_LUHN_ALGORITHM_DIGIT:
                total_checksum += (int(reverse_card_number[index]) * 2 - MAX_LUHN_ALGORITHM_DIGIT)
            else:
                total_checksum += int(reverse_card_number[index]) * 2

        index += 1

    if (int(total_checksum + last_card_digit)) % MULTIPLE_OF_TEN == 0:
        return 'Authentic'

    return 'Fake'
