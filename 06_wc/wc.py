#!/usr/bin/env python3


"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Word Count
Method: We're going to use a dictionary as a lookup for any numbers that appear in the given string.
"""

import argparse
import sys


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="wc.py",
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "files",
        metavar="FILES",
        nargs="*",
        default=[sys.stdin],
        type=argparse.FileType("rt"),
        help="Input file(s)",
    )

    return parser.parse_args()


def main():
    """Looping through files and printing line, word, character count"""
    args = get_args()

    total_lines, total_words, total_chars = 0, 0, 0

    for file in args.files:
        lines, words, chars = 0, 0, 0
        for line in file:
            lines += 1
            words += len(line.split())
            chars += len(line)

        total_lines += lines
        total_words += words
        total_chars += chars

        print(f"{lines:8}{words:8}{chars:8} {file.name}")

    if len(args.files) > 1:
        print(f"{total_lines:8}{total_words:8}{total_chars:8} total")


if __name__ == "__main__":
    main()
