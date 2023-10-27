#!/usr/bin/env python3

import argparse
import os


def is_valid_file(arg):
    if not os.path.exists(arg):
        raise argparse.ArgumentTypeError(f"{arg} does not exist.")
    return arg


parser = argparse.ArgumentParser()
parser.add_argument("--input", type=is_valid_file, help="Input file or string")

args = parser.parse_args()

if os.path.isfile(args.input):
    # It's a file
    with open(args.input, "r") as file:
        content = file.read()
else:
    # It's a regular string
    content = args.input

# Now you can work with the 'content' variable, which contains either the file's content or the string argument.

"""
ChatGPT gave this as the answer to the question "what if I want to accept either a string or file in an argparse argument?".
The code is wrong, since it will not accept a string as an argument in the command line. 
Providing a string raises the error in the is_valid_file function and the program won't move forward.
Pointed this out and it removed the raise error line and replaced with a return arg line. 
So it was doing a redundant check on the input type, which it corrected after further prompting.
It was broadly correct in how it thought through the code, and correctly noted that argparse accepts a UDF in the 'type' variable.
"""
