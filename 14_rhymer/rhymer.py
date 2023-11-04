#!/usr/bin/env python3

"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Ransom Note
Method: Capitalize random letters of a line, from either the CLI or a given file.
"""

import argparse
import re

prefixes = (
    list("bcdfghjklmnpqrstvwxyz")
    + (
        "bl br ch cl cr dr fl fr gl gr pl pr sc "
        "sh sk sl sm sn sp st sw th tr tw thw wh wr "
        "sch scr shr sph spl spr squ str thr"
    ).split()
)


def get_args():
    parser = argparse.ArgumentParser(
        prog="rhymer.py",
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "str",
        metavar="str",
        type=str,
        help="A word to rhyme",
    )

    return parser.parse_args()


def suffix(text):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    pattern = f"([{consonants}]+)?([{vowels}])(.*)"

    regex = re.match(pattern, text)
    if regex:
        p1 = regex.group(1) or ""
        p2 = regex.group(2) or ""
        p3 = regex.group(3) or ""
        return (p1, p2 + p3)
    else:
        return (regex, "")


def main():
    text = get_args().str.lower()

    first, rest = suffix(text)
    if rest:
        print("\n".join(sorted([p + rest for p in prefixes if p != first])))
    else:
        print(f'Cannot rhyme "{get_args().str}"')


if __name__ == "__main__":
    main()
