#!/usr/bin/env python3
"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Ransom Note
Method: Capitalize random letters of a line, from either the CLI or a given file.
"""

import argparse
import os
import re


def get_args():
    parser = argparse.ArgumentParser(
        prog="friar.py",
        description="Souther fry text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "text",
        metavar="text",
        help="Input text or file",
    )

    return parser.parse_args()


def replacer(text):
    you = re.match("([Yy])ou$", text)
    ing = re.search("(.+)ing$", text)

    if ing:
        prefix = ing.group(1)
        if re.search("[aeiouy]", prefix, re.IGNORECASE):
            return prefix + "in'"
    elif you:
        return you.group(1) + "'all"

    return text


def main():
    args = get_args()

    if os.path.exists(args.text):
        with open(args.text) as file:
            content = file.read()
    else:
        content = args.text

    for line in content.splitlines():
        print("".join(map(replacer, re.split(r"(\W+)", line.rstrip()))))


if __name__ == "__main__":
    main()
