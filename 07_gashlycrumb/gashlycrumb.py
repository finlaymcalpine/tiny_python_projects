#!/usr/bin/env python3


"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Line Finder
Method: We use a dict comp to create a lookup table for the lines in the given file. If the first character matches a given letter, we print the line.
If not, print 'I do not know "letter"'.
"""

import argparse


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="gashlycrumb.py",
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "letter",
        metavar="letter",
        nargs="+",
        help="Letter(s)",
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="FILE",
        # nargs="*",
        default="gashlycrumb.txt",
        type=argparse.FileType(
            "r"
        ),  # NB this method doesn't handle files well, and can leave them open. Use open() for better implementation.
        help="Input file",
    )

    return parser.parse_args()


def main():
    """"""
    args = get_args()

    lines = {line[0].upper(): line.rstrip() for line in args.file}

    for i in args.letter:
        print(lines.get(i.upper(), f'I do not know "{i}".'))


if __name__ == "__main__":
    main()
