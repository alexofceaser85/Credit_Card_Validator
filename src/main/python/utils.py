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

        if (len(card_digits_group) < minimum_card_length or len(card_digits_group) > maximum_card_length):
            return False

        if (len(card_digits_group) == four_digit_subgroup_card_length):
            four_digit_group_regex = re.compile(r'^(\d{4})+(-|\s)?(\d{4})+(-|\s)?(\d{4})+(-|\s)?(\d{4})$')
            four_digit_group_match = four_digit_group_regex.search(sequence)
            return True 

        return True

    else:
        return False

def luhn_verified(credit_card_number):
    """
    This function uses the luhn algorithm to determine if a given credit card number is a fake or an authentic
    card number
    """
    credit_card_digits = credit_card_number.replace(' ','').replace('-','')
    dropped_last_digit = credit_card_digits[:len(credit_card_digits) - 1]
    last_card_digit = int(credit_card_digits[(len(credit_card_digits) - 1):len(credit_card_digits)])
    reverse_card_number = dropped_last_digit[::-1]

    total_checksum = 0
    index = 0
     
    while(index < len(reverse_card_number)):
        
        if(index % 2 != 0):
            total_checksum += int(reverse_card_number[index])
        else:
            if ((int(reverse_card_number[index]) * 2) > 9):
                total_checksum += (int(reverse_card_number[index]) * 2 - 9)
            else:
                total_checksum += int(reverse_card_number[index]) * 2
        
        index += 1
   
    if (int(total_checksum + last_card_digit)) % 10 == 0:
        return 'Authentic'
    else:
        return 'Fake'
