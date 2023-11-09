#!/usr/bin/env python3

"""

"""

import argparse
import os
import re


def file_string_parser(arg):
    if os.path.exists(arg):
        with open(arg) as file:
            content = file.read().rstrip()
    else:
        content = arg

    return content


def get_args():
    parser = argparse.ArgumentParser(
        prog="gematria.py",
        description="Gematria",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "input",
        metavar="str",
        type=file_string_parser,
        help="Input text or file",
    )

    return parser.parse_args()


def word_convertor(word):
    """summation of ordinal values for word characters, restricted to a-z and 0-9"""
    relevant_chars = re.sub("[^a-zA-Z0-9]", "", word)
    word_total = sum([ord(i) for i in relevant_chars])
    return str(word_total)


def main():
    args = get_args()

    for line in args.input.splitlines():
        output = " ".join(map(word_convertor, line.split()))
        print(output)


if __name__ == "__main__":
    main()
