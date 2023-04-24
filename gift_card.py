"""
Gift Card Problem
You have been given a gift card that is about to expire and you want to buy gifts for 2 friends.

You want to spend the whole gift card, or if that’s not an option as close to the balance as
possible. You have a list of sorted prices for a popular store that you know both friends like to
shop at. Your challenge is to find two distinct items in the list whose sum is minimally under (or
equal to) the gift card balance.

The file contains two columns:
A unique identifier of the item
The value of that item in cents. It is always a positive integer that represents the price in
cents (1000 = $10.00 USD). You can assume every item in the store has a unique price.

Write a program to find the best two items. It takes two inputs:
A filename with a list of sorted prices
The balance of your gift card in cents

If no two items have a sum that is less than or equal to the balance on the gift card, print “Not
possible”. Don’t return every possible pair that is under the balance, just one optimal pair.

Examples:

$ cat prices.txt
Candybar, 500
Book, 700
Detergent, 1000
Headphones, 1400
Earmuffs, 2000
Speaker, 6000

$ find-pair prices.txt 2500
Candybar 500, Earmuffs 2000

$ find-pair prices.txt 2300
Book 700, Headphones 1400

$ find-pair prices.txt 10000
Earmuffs 2000, Speaker 6000

$ find-pair prices.txt 1100
Not possible
"""

import argparse
import subprocess


def find_pair(filename, balance):
    # parse file, assumes items will fit into memory
    prices = []
    with open(filename) as f:
        for line in f:
            item, price = line.strip().split(", ")
            prices.append((item, int(price)))

    # i and j are indices into the beginning and end of the price list respectively
    i = 0
    j = len(prices) - 1
    # this will keep track of the pair with the largest sum we've seen so far
    best_pair = None
    while i < j:
        if prices[i][1] + prices[j][1] <= balance:
            if (
                best_pair is None
                or prices[i][1] + prices[j][1] > best_pair[1][1] + best_pair[0][1]
            ):
                best_pair = (prices[i], prices[j])
            i += 1
        else:
            j -= 1

    if best_pair is None:
        print("Not possible")
    else:
        print(
            f"{best_pair[0][0]} {best_pair[0][1]}, {best_pair[1][0]} {best_pair[1][1]}"
        )


def find_triplet(filename, balance):
    prices = []
    with open(filename, "r") as f:
        for line in f:
            item_id, price = line.strip().split(",")
            price = int(price)
            # only add items that are less than the balance this time
            if price <= balance:
                prices.append((item_id, price))

    n = len(prices)
    if n < 3:
        print("Not possible")
        return

    best_sum = -1
    best_triplet = None
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sum = prices[i][1] + prices[j][1] + prices[k][1]
                if sum == balance:
                    print(
                        f"{prices[i][0]} {prices[i][1]}, {prices[j][0]} {prices[j][1]}, {prices[k][0]} {prices[k][1]}"
                    )
                    return
                elif sum < balance and sum > best_sum:
                    best_sum = sum
                    best_triplet = (prices[i], prices[j], prices[k])

    if best_triplet is None:
        print("Not possible")
    else:
        print(
            f"{best_triplet[0][0]} {best_triplet[0][1]}, {best_triplet[1][0]} {best_triplet[1][1]}, {best_triplet[2][0]} {best_triplet[2][1]}"
        )


def test_find_pair():
    print("Running tests...")

    print("Test 1 - prices.txt, 2500")
    output = subprocess.check_output(["python", "gift_card.py", "prices.txt", "2500"])
    assert output == b"Candybar 500, Earmuffs 2000\n"
    print("\tPassed")

    print("Test 2 - prices.txt, 2300")
    output = subprocess.check_output(["python", "gift_card.py", "prices.txt", "2300"])
    assert output == b"Book 700, Headphones 1400\n"
    print("\tPassed")

    print("Test 3 - prices.txt, 10000")
    output = subprocess.check_output(["python", "gift_card.py", "prices.txt", "10000"])
    assert output == b"Earmuffs 2000, Speaker 6000\n"
    print("\tPassed")

    print("Test 4 - prices.txt, 1100")
    output = subprocess.check_output(["python", "gift_card.py", "prices.txt", "1100"])
    assert output == b"Not possible\n"
    print("\tPassed")

    print("All tests passed!")


def test_find_triplet():
    print("Running tests...")

    print("Test 1 - prices.txt, 2500, 3 gifts")
    output = subprocess.check_output(
        ["python", "gift_card.py", "prices.txt", "2500", "--num_gifts", "3"]
    )
    assert output == b"Candybar 500, Book 700, Detergent 1000\n"
    print("\tPassed")

    print("Test 2 - prices.txt, 2300, 3 gifts")
    output = subprocess.check_output(
        ["python", "gift_card.py", "prices.txt", "2300", "--num_gifts", "3"]
    )
    assert output == b"Candybar 500, Book 700, Detergent 1000\n"
    print("\tPassed")

    print("Test 3 - prices.txt, 10000, 3 gifts")
    output = subprocess.check_output(
        ["python", "gift_card.py", "prices.txt", "10000", "--num_gifts", "3"]
    )
    assert output == b"Headphones 1400, Earmuffs 2000, Speaker 6000\n"
    print("\tPassed")

    print("Test 4 - prices.txt, 1100, 3 gifts")
    output = subprocess.check_output(
        ["python", "gift_card.py", "prices.txt", "1100", "--num_gifts", "3"]
    )
    assert output == b"Not possible\n"
    print("\tPassed")

    print("Test 5 - prices.txt, 7700, 3 gifts")
    output = subprocess.check_output(
        ["python", "gift_card.py", "prices.txt", "7700", "--num_gifts", "3"]
    )
    assert output == b"Book 700, Detergent 1000, Speaker 6000\n"
    print("\tPassed")

    print("All tests passed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Find the best pair of items to buy with a gift card"
    )
    parser.add_argument("filename", help="File containing list of items and prices")
    parser.add_argument("balance", type=int, help="Balance of gift card in cents")
    parser.add_argument(
        "--num_gifts",
        type=int,
        default=2,
        help="The number of gifts to select (2 or 3, default=2)",
    )
    args = parser.parse_args()

    if args.num_gifts == 2:
        # pairs
        if args.filename != "" and args.balance >= 0:
            find_pair(args.filename, args.balance)
        else:
            test_find_pair()
    elif args.num_gifts == 3:
        # triplets
        if args.filename != "" and args.balance >= 0:
            find_triplet(args.filename, args.balance)
        else:
            test_find_triplet()
    else:
        print("Invalid number of gifts")
