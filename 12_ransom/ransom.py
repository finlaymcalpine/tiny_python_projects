#!/usr/bin/env python3


"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Ransom Note
Method: Capitalize random letters of a line, from either the CLI or a given file.
"""

import argparse
import os
import random


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="ransom.py",
        description="RansomNote",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "input",
        metavar="str",
        help="Input text or file",
    )
    parser.add_argument(
        "-s",
        "--seed",
        metavar="SEED",
        type=int,
        default=None,
        help="Random seed",
    )

    return parser.parse_args()


def replacer(char):
    """"""
    return char.upper() if random.choice([0, 1]) else char.lower()


def main():
    """"""
    args = get_args()

    random.seed(args.seed)

    if os.path.exists(args.input):
        with open(args.input) as file:
            content = file.read()
    else:
        content = args.input

    output = "".join(map(replacer, content))

    """ could also do the following:
    output = "".join([replacer(i) for i in content])
    """

    print(output)


if __name__ == "__main__":
    main()
