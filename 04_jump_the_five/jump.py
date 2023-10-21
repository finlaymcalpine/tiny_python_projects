#!/usr/bin/env python3

"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Encoding given number by "'crossing the five' on a telephone keypad.
Method: We're going to use a dictionary as a lookup for any numbers that appear in the given string.
We recreate the string in a new list, by iterating through the characters of the input string and either re-encoding or leaving unchanged if not a number.
"""

import argparse

encoding_key = {
    "0": "5",
    "1": "9",
    "2": "8",
    "3": "7",
    "4": "6",
    "5": "0",
    "6": "4",
    "7": "3",
    "8": "2",
    "9": "1",
}


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="jump.py",
        description="Jumping Over the Five - number encoding",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "string",
        metavar="str",
        help="Input for the program",
    )
    return parser.parse_args()


def main():
    args = get_args()
    input_str = args.string
    output_str = [encoding_key.get(i, i) for i in input_str]
    print(f"{''.join(output_str)}")


if __name__ == "__main__":
    main()
