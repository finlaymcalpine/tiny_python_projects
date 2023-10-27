#!/usr/bin/env python3

"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Encoding given number by "'crossing the five' on a telephone keypad.
Method: We're going to use a dictionary as a lookup for any numbers that appear in the given string.
"""

import os
import argparse
import sys


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="howler.py",
        description="Uppercase Text - printing or writing to a file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "string",
        metavar="str",
        type=str,
        help="Input for the program",
    )
    parser.add_argument(
        "-o",
        "--outfile",
        metavar="outfile",
        type=str,
        help="Destination file for output.",
    )
    return parser.parse_args()


def read_input(a):
    input_string = a.string
    if os.path.isfile(input_string):
        upper_file = open(input_string).read().rstrip().upper() + "\n"
        return upper_file
    else:
        upper_text = input_string.upper() + "\n"
        return upper_text


def main():
    args = get_args()
    output_string = read_input(args)
    out_file = open(args.outfile, "wt") if args.outfile else sys.stdout
    out_file.write(output_string)
    out_file.close()


if __name__ == "__main__":
    main()
