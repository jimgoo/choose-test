"""
Combinations Problem

You are given a string composed of only 1s, 0s, and Xs.

Write a program that will print out every possible combination where you replace the X with both 0 and 1.

Examples:

$ combinations X0
00
10

$ combinations 10X10X0
1001000
1001010
1011000
1011010
"""

import argparse
import subprocess
import sys


def combinations(s):
    # count the number of Xs in the string
    x_count = s.count("X")
    # count up to the number of combinations
    for i in range(2**x_count):
        # binary representation of i
        bin_str = bin(i)[2:].zfill(x_count)
        # replaces X with the corresponding value from the binary string
        comb = s.replace("X", "{}").format(*bin_str)
        print(comb)


def test_combinations():
    print("Running tests...")

    print("Test 1 - X0")
    output = subprocess.check_output(["python", "combinations.py", "X0"])
    assert output == b"00\n10\n"
    print("\tPassed")

    print("Test 2 - 10X10X0")
    output = subprocess.check_output(["python", "combinations.py", "10X10X0"])
    assert output == b"1001000\n1001010\n1011000\n1011010\n"
    print("\tPassed")

    print("All tests passed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Print all combinations of a string with Xs replaced by 0 and 1"
    )
    parser.add_argument("input_string", type=str, help="String with Xs to be replaced")
    args = parser.parse_args()
    # validate input
    for c in args.input_string:
        if c not in ["0", "1", "X"]:
            print(f"Invalid input character, should be 0, 1, or X but found: {c}")
            sys.exit(1)

    if args.input_string != "":
        combinations(args.input_string)
    else:
        test_combinations()
