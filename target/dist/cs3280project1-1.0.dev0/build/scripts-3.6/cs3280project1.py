#!python

"""
This is the main class for the program, it accepts a location for a file containing card data
and determines if the card is of the correct format, the card issuer, and if the card is authentic
"""


import sys
import re
from pathlib import Path
sys.path.append('../python')
print(sys.path)
import utils

__author__ = "Alex DeCesare"
__version__ = "12-September-2020"

FILE_LOCATION = Path(sys.argv[1])
CREDIT_CARD_LIST = []

def main():
    """
    This is the main method of the program, calls the methods to determine if a card is the correct
    format, the card issuer, and if the card is authentic
    """
    print('Please enter a credit card number')
    credit_card_number = input()

    output_credit_card_number = "Invalid"
    output_credit_card_type = "Invalid"
    output_luhn_verification = "N/A"

    if utils.is_valid(credit_card_number):

        credit_card_digits = extract_credit_card_digits(credit_card_number)

        parse_credit_card_file()
        equal_card_length = find_matching_card_length(credit_card_digits)
        found_credit_card = find_matching_start_digits(equal_card_length, credit_card_digits)

        output_credit_card_number = credit_card_number
        output_luhn_verification = utils.is_luhn_verified(credit_card_number)

        if found_credit_card is not None:
            output_credit_card_type = found_credit_card['card_issuer']

    print(
        "Credit card number:  " + output_credit_card_number + "\n"
        + "Credit card type:    " + output_credit_card_type + "\n"
        + "Luhn verification:   " + output_luhn_verification + "\n"
    )

def parse_credit_card_file():

    """
    parses the cards in the credit card types file and retrives the required information and adds
    the new card to the credit card list variable
    """
    try:
        card_file = open(FILE_LOCATION, 'r')
        card_file_contents = card_file.readlines()

        for current_card in card_file_contents:
            current_card_properties = current_card.split(';')

            credit_card = {
                'card_issuer' : current_card_properties[0],
                'card_length' : current_card_properties[1].split(','),
                'card_start_digits' : remove_new_line_tag(current_card_properties[2].split(','))
            }

            CREDIT_CARD_LIST.append(credit_card)

    except FileNotFoundError as file_not_found_exception:
        print(file_not_found_exception)

def find_matching_card_length(credit_card_number):

    """
    Returns all of the cards in the credit card types file that requires the same length as the
    length of the inputted credit card number
    """

    matching_cards = []

    for current_card in CREDIT_CARD_LIST:

        for current_card_length in current_card['card_length']:

            if int(current_card_length) == len(credit_card_number):

                matching_cards.append(current_card)

    return matching_cards

def find_matching_start_digits(credit_cards, credit_card_number):

    """
    Finds the credit card in the credit cards types list that have the same starting numbers
    as the inputted credit card number
    """

    for current_card in credit_cards:

        for current_card_data_start_digits in current_card['card_start_digits']:

            if '-' in current_card_data_start_digits:
                start_digits_range = current_card_data_start_digits.split('-')
                minimum_digit = start_digits_range[0]
                maximum_digit = start_digits_range[1]

                minimum_start_digits = credit_card_number[0:len(minimum_digit)]
                maximum_start_digits = credit_card_number[0:len(maximum_digit)]

                if minimum_start_digits >= minimum_digit and maximum_start_digits <= maximum_digit:
                    return current_card
            else:
                card_number_start_digits = credit_card_number[:len(current_card_data_start_digits)]

            if card_number_start_digits == current_card_data_start_digits:
                return current_card
    return None

def extract_credit_card_digits(credit_card_number):

    """
    removes all of the digits from the already valid card number
    """

    card_digits = re.findall(r'\d+', credit_card_number)
    card_number = ''.join(card_digits)

    return card_number

def remove_new_line_tag(card_start_digits):

    """
    Removes the new line tag from the elements in a given array
    """

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
