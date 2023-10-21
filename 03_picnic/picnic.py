#!/usr/bin/env python3

"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: 
"""

import argparse


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="picnic.py",
        description="Picnic Basket - listing items to be taken",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "string",
        nargs="+",
        metavar="str",
        help="Word(s) for the program",
    )
    parser.add_argument(
        "-s",
        "--sorted",
        action="store_true",
        help="Output sorted if included",
    )
    return parser.parse_args()


def main():
    args = get_args()
    input_words = args.string
    if args.sorted:
        input_words.sort()
    if len(input_words) == 1:
        items = input_words[0]
    elif len(input_words) == 2:
        items = " and ".join(input_words)
    elif len(input_words) >= 3:
        items = ", ".join(input_words[:-1]) + ", and " + input_words[-1]
    print(f"You are bringing {items}.")


if __name__ == "__main__":
    main()
