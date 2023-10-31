#!/usr/bin/env python3

"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Bottles of Beer Song
Method: Print lines from 99 Bottles of Beer from given number down
"""

import argparse


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        prog="telephone.py",
        description="StringMutation",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-n",
        "--num",
        metavar="NUMBER",
        default=10,
        type=int,
        help="How many bottles",
    )

    checks = parser.parse_args()

    if checks.num < 1:
        parser.error(f'--num "{checks.num}" must be greater than 0')

    return checks


def main():
    args = get_args()

    for i in range(args.num, 0, -1):
        plural = "s" if i > 1 else ""
        last_plural = "s" if i != 2 else ""
        next_number = "No more" if i == 1 else i - 1
        print(
            "\n".join(
                [
                    f"{i} bottle{plural} of beer on the wall,",
                    f"{i} bottle{plural} of beer,",
                    f"Take one down, pass it around,",
                    f"{next_number} bottle{last_plural} of beer on the wall!",
                ]
            )
        )
        if i != 1:
            print("")
        else:
            pass


if __name__ == "__main__":
    main()
