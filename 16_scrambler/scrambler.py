#!/usr/bin/env python3

import argparse
import random
import os
import re


def get_args():
    parser = argparse.ArgumentParser(
        prog="scrambler.py",
        description="Scramble the letters of words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-s",
        "--seed",
        metavar="SEED",
        type=int,
        default=None,
        help="Random seed",
    )

    parser.add_argument(
        "input",
        metavar="str",
        help="Input text or file",
    )

    return parser.parse_args()


def scrambler(word):
    """
    If word is 3 or fewer chars, no shuffling. If more than 3 chars, shuffle elements of string not at start or end index
    """
    if len(word) <= 3:
        return word
    else:
        shuffled_chars = list(word[1:-1])
        random.shuffle(shuffled_chars)
        word = word[0] + ("".join(shuffled_chars)) + word[-1]
        return word


def main():
    """
    Parse args, set seed, set string to be scrambled as the content variable.
    """
    args = get_args()
    random.seed(args.seed)
    split_point = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    # we're creating an expression to split on words, and retain spaces/periods as seperate components for the join later

    if os.path.exists(args.input):
        with open(args.input) as file:
            content = file.read().rstrip()
    else:
        content = args.input

    for line in content.splitlines():
        print("".join(map(scrambler, split_point.split(line))))


if __name__ == "__main__":
    main()
