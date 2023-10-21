#!/usr/bin/env python3

"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: print "Hello, World!" by default, but print "Hello, Name!" if an optional argument "Name" is provided in the CLI.
"""

import argparse


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="hello.py",
        description="Prints a hello to the input",
    )
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        default="World",
        help="Name to greet (default: World)",
    )
    return parser.parse_args()


def main():
    """Standard main entry"""
    args = get_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
