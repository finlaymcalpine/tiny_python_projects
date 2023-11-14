#!/usr/bin/env python3

"""

"""

import argparse
import os
import random
import pandas as pd
import numpy as np
from tabulate import tabulate


def file_string_parser(arg):
    if os.path.exists(arg) and arg[-4:-1] == ".csv":
        return pd.read_csv(arg)
    else:
        raise argparse.ArgumentTypeError(f'--file "{arg}" must be .csv type')


def get_args():
    parser = argparse.ArgumentParser(
        prog="wod.py",
        description="Create Workout Of (the) Day (WOD)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        metavar="str",
        default="inputs/exercises.csv",
        type=argparse.FileType("r"),
        help="CSV input file of exercises",
    )

    parser.add_argument(
        "-s",
        "--seed",
        metavar="int",
        default=None,
        help="Random seed",
    )

    parser.add_argument(
        "-n",
        "--num",
        metavar="int",
        type=int,
        default=4,
        help="Number of exercises",
    )

    parser.add_argument(
        "-e",
        "--easy",
        metavar="",
        type=bool,
        default=False,
        help="Halve the reps",
    )

    checks = parser.parse_args()

    if checks.num < 1:
        parser.error(f'--num "{checks.num}" must be greater than 0')

    return checks


def read_csv(input):
    df = pd.read_csv(input).dropna()
    df.rename(columns={"exercise": "Exercise"}, inplace=True)
    df["min"] = df.reps.str.extract(r"(\d+)\-").astype("int")
    df["max"] = df.reps.str.extract(r"\-(\d+)").astype("int")
    return df


def main():
    args = get_args()
    random.seed(args.seed)
    rng = np.random.default_rng(int(args.seed))
    factor = 0.5 if args.easy else 1

    inputs = read_csv(args.file)
    inputs["Reps"] = (
        (factor * rng.integers(inputs["min"], inputs["max"], endpoint=True))
        .round()
        .astype("int")
    )
    outputs = inputs.sample(args.num, random_state=rng)

    print(tabulate(outputs[["Exercise", "Reps"]], headers="keys", showindex=False))


if __name__ == "__main__":
    main()
