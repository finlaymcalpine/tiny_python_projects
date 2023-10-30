#!/usr/bin/env python3

"""
Author: Finlay McAlpine <finlay.mcalpine1@gmail.com>
Purpose: Apples and Bananas
Method:
"""

import argparse
import random


def get_args():
    """Get command line arguments and check given args to ensure > 0"""

    parser = argparse.ArgumentParser(
        prog="abuse.py",
        description="Heap Abuse",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--number",
        metavar="NUMBER",
        default=3,
        type=int,
        help="Number of insults",
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        metavar="ADJECTIVES",
        default=2,
        type=int,
        help="Number of adjectives",
    )

    parser.add_argument(
        "-s",
        "--seed",
        metavar="SEED",
        default=None,
        type=int,
        help="Random seed",
    )

    value_checks = parser.parse_args()

    if value_checks.number <= 0:
        parser.error(f'--number "{value_checks.number}" must be > 0')

    if value_checks.adjectives <= 0:
        parser.error(f'--adjectives "{value_checks.adjectives}" must be > 0')

    return value_checks


def main():
    """"""
    args = get_args()

    num_insults, num_adjectives = args.number, args.adjectives

    random.seed(args.seed)

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.strip().split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.strip().split()

    for i in range(num_insults):
        random_adjs = ", ".join(random.sample(adjectives, k=num_adjectives))
        print(f"You {random_adjs} {random.choice(nouns)}!")


if __name__ == "__main__":
    main()
