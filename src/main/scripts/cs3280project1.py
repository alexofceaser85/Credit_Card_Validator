#!/usr/bin/env python3

"""
This is the main class for the program, it accepts a location for a file containing card data and determines if the
card is of the correct format, the card issuer, and if the card is authentic
"""
import sys
sys.path.append('../python')
import utils
import os
from pathlib import Path

__author__ = "Alex DeCesare"
__version__ = "12-September-2020"

file_location = Path('../../../docs/credit_card_types.ssv')
credit_card_list = []

def main():
    """
    This is the main method of the program, calls the methods to determine if a card is the correct format, the card     issuer, and if the card is authentic
    """
    print('Please enter a credit card number')
    credit_card_number = input()

    parse_credit_card_file()
    equal_card_length = find_matching_card_length(credit_card_number)

def parse_credit_card_file():

    """
    parses the cards in the credit card types file and retrives the required information and adds the new card
    to the credit card list variable
    """

    card_file = open(file_location, 'r')
    card_file_contents = card_file.readlines()

    for current_card in card_file_contents:
        current_card_properties = current_card.split(';')
        
        credit_card = {
                'card_issuer' : current_card_properties[0],
                'card_length' : current_card_properties[1].split(','),
                'card_start_digits' : remove_new_line_tag(current_card_properties[2].split(','))
                }

        credit_card_list.append(credit_card)

def find_matching_card_length(credit_card_number):

    matching_cards = []

    for current_card in credit_card_list:

        for current_card_length in current_card['card_length']:

            if int(current_card_length) == len(credit_card_number):

                matching_cards.append(current_card)

def remove_new_line_tag(card_start_digits):
    
    formatted_card_start_digits = []

    for start_digit in card_start_digits:
        
        if '\n' in start_digit:
            remove_new_line = start_digit.replace('\n', '')
            formatted_card_start_digits.append(remove_new_line)
        else:
            formatted_card_start_digits.append(start_digit)
    return formatted_card_start_digits

if __name__ == '__main__':
    main()
