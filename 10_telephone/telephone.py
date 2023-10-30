#!/usr/bin/env python3

"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Telephone
Method: Randomly change characters in a given string, where proportion of altered characters is an optionally given percentage between 0 and 1.
"""

import argparse
import os
import random
import string


def restricted_float(x):
    try:
        x = float(x)
    except ValueError:
        raise argparse.ArgumentTypeError(f"invalid float value: '{x}'")

    if x < 0.0 or x > 1.0:
        raise argparse.ArgumentTypeError(f'--mutations "{x}" must be between 0 and 1')
    return x


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="telephone.py",
        description="StringMutation",
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
        default=None,
        type=int,
        help="Random seed",
    )
    parser.add_argument(
        "-m",
        "--mutations",
        metavar="MUTATIONS",
        default=0.1,
        type=restricted_float,
        help="Percent mutations",
    )

    return parser.parse_args()


def main():
    """
    Will loop through given string and change character if a random draw is less than the mutation percentage.
    Available characters for random draw are from string package.
    """
    args = get_args()

    random.seed(args.seed)

    characters = string.ascii_letters + string.punctuation

    if os.path.exists(args.input):
        with open(args.input) as file:
            content = file.read()
    else:
        content = args.input

    output = ""

    for i in content:
        if random.uniform(0.0, 1.0) < args.mutations:
            output += random.choice(characters)
        else:
            output += i

    print(f'You said: "{content}"\nI heard : "{output}"')


if __name__ == "__main__":
    main()
