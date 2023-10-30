#!/usr/bin/env python3


"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Apples and Bananas
Method:
"""

import argparse
import os
# import re


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="apples.py",
        description="VowelReplacement",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "input",
        metavar="str",
        help="Input text or file",
    )
    parser.add_argument(
        "-v",
        "--vowel",
        metavar="str",
        default="a",
        choices=["a", "e", "i", "o", "u"],
        help="The vowel to substitute",
    )

    return parser.parse_args()


def main():
    """"""
    args = get_args()

    if os.path.exists(args.input):
        with open(args.input) as file:
            content = file.read()
    else:
        content = args.input

    def vowel_replacer(char):
        return (
            args.vowel
            if char in "aeiou"
            else args.vowel.upper()
            if char in "AEIOU"
            else char
        )

    output = "".join(map(vowel_replacer, content))

    print(output)

    """
    below method didn't retain the case of the original string vowel and replaced with a lowercase letter.
    regex is a valid way to do this, but would have to split to two regexes, for upper and lowercase letters.
    something like the vowel_replacer function above.
    """
    # print(f"{re.sub(r'[aeiouAEIOU]', str(vowel), content)}")


if __name__ == "__main__":
    main()
