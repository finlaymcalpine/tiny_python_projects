#!/usr/bin/env python3

"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Announcing sights "off the larboard bow"
"""

import argparse


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="crowsnest.py",
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "word",  # no dashes here means it's a positional argument and not keyword
        metavar="str",
        help="A word for the program",
    )
    return parser.parse_args()


def main():
    args = get_args()
    word = args.word
    article = "an " if word[0].lower() in "aeiou" else "a "
    print(f"Ahoy, Captain, {article + word} off the larboard bow!")


if __name__ == "__main__":
    main()
