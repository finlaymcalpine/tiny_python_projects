#!/usr/bin/env python3

"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Twelve Days of Christmas Printer
Method: 
"""

import os
import argparse
import sys

line_dict = {
    1: ("first", "A partridge in a pear tree."),
    2: ("second", "Two turtle doves,"),
    3: ("third", "Three French hens,"),
    4: ("fourth", "Four calling birds,"),
    5: ("fifth", "Five gold rings,"),
    6: ("sixth", "Six geese a laying,"),
    7: ("seventh", "Seven swans a swimming,"),
    8: ("eighth", "Eight maids a milking,"),
    9: ("ninth", "Nine ladies dancing,"),
    10: ("tenth", "Ten lords a leaping,"),
    11: ("eleventh", "Eleven pipers piping,"),
    12: ("twelfth", "Twelve drummers drumming,"),
}


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="twelve_days.py",
        description="Printing or writing verses of 12 Days of Christmas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-n",
        "--num",
        metavar="NUMBER",
        type=int,
        default=12,
        help="Number of days to sing",
    )
    parser.add_argument(
        "-o",
        "--outfile",
        metavar="FILE",
        type=str,
        help="Outfile",
    )

    checks = parser.parse_args()

    if checks.num < 1 or checks.num > 12:
        parser.error(f'--num "{checks.num}" must be between 1 and 12')
    else:
        pass

    return checks


def create_verse(verse):
    items = [line_dict[i][1] for i in range(verse, 0, -1)]

    if verse > 1:
        items[-1] = "And " + items[-1].lower()

    return "\n".join(
        [
            f"On the {line_dict[verse][0]} day of Christmas,",
            "My true love gave to me,",
        ]
        + items
    )


def main():
    args = get_args()
    output_string = "\n\n".join([create_verse(i) for i in range(1, args.num + 1)])
    out_file = open(args.outfile, "w") if args.outfile else sys.stdout
    out_file.write(output_string)
    out_file.close()


if __name__ == "__main__":
    main()
