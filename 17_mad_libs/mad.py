#!/usr/bin/env python3

import argparse
import re
import sys


def get_args():
    parser = argparse.ArgumentParser(
        prog="mad.py",
        description="Mad Libs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        help="Input file",
        type=argparse.FileType("r"),
    )

    parser.add_argument(
        "-i",
        "--inputs",
        metavar="str",
        help="Inputs (for testing)",
        default=None,
        type=str,
        nargs="*",
    )

    return parser.parse_args()


def main():
    args = get_args()
    inputs = args.inputs
    content = args.file.read().rstrip()
    placeholders = re.findall("(<([^<>]+)>)", content)

    if not placeholders:
        sys.exit(f'"{args.file.name}" has no placeholders.')

    request = "Give me {} {}: "
    for placeholder, p in placeholders:
        a_an = "an" if p.lower()[0] in "aeiou" else "a"
        response = inputs.pop(0) if inputs else input(request.format(a_an, p))
        content = re.sub(placeholder, response, content, count=1)

    print(content)


if __name__ == "__main__":
    main()
