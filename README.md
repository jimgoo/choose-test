# Coding Challenge - Takehome Test

## Setup

You just need python, no other dependencies. I used Python 3, but Python 2 should work.

## Combinations Problem

```
$ python combinations.py --help
usage: combinations.py [-h] input_string

Print all combinations of a string with Xs replaced by 0 and 1

positional arguments:
  input_string  String with Xs to be replaced

optional arguments:
  -h, --help    show this help message and exit
```

Run an example

```
$ python combinations.py X0
00
10
```

Run all examples and verify output is correct

```
$ python combinations.py ""
Running tests...
Test 1 - X0
        Passed
Test 2 - 10X10X0
        Passed
All tests passed!
```

The time complexity is O(2^n), where n is the number of Xs in the input string. This is because there are 2 possible values (0 or 1) for each X, and we need to generate all possible combinations of these values, which is 2^n. The space complexity is O(1), as we only need to store the input string and some variables to generate the combinations.

## Gift Card Problem

```
$ python gift_card.py --help
usage: Find the best pair of items to buy with a gift card [-h] [--num_gifts NUM_GIFTS] filename balance

positional arguments:
  filename              File containing list of items and prices
  balance               Balance of gift card in cents

optional arguments:
  -h, --help            show this help message and exit
  --num_gifts NUM_GIFTS
                        The number of gifts to select (2 or 3, default=2)
```

Find the best pair:

```
$ python gift_card.py prices.txt 2300
Book 700, Headphones 1400
```

Find the best triplet:

```
$ python gift_card.py prices.txt 2300 --num_gifts 3
Candybar 500, Book 700, Detergent 1000
```

Run all examples and verify output is correct for pairs:

```
$ python gift_card.py "" -1
Running tests...
Test 1 - prices.txt, 2500
        Passed
Test 2 - prices.txt, 2300
        Passed
Test 3 - prices.txt, 10000
        Passed
Test 4 - prices.txt, 1100
        Passed
All tests passed!
```

Run all examples and verify output is correct for triplets:

```
$ python gift_card.py "" -1 --num_gifts 3
Running tests...
Test 1 - prices.txt, 2500, 3 gifts
        Passed
Test 2 - prices.txt, 2300, 3 gifts
        Passed
Test 3 - prices.txt, 10000, 3 gifts
        Passed
Test 4 - prices.txt, 1100, 3 gifts
        Passed
Test 5 - prices.txt, 7700, 3 gifts
        Passed
All tests passed!
```

The `find_pair` method reads in the file of prices and stores them as a list of `(id, price)` tuples. It then uses a two-pointer approach to find the best pair of items. It starts with the first and last prices and moves the pointers inward until it finds a pair whose sum is equal to the balance or until the pointers meet. If a pair with the exact balance is found, it is returned. Otherwise, the program keeps track of the best pair found so far whose sum is less than the balance.

The time complexity of the program is O(n), where n is the number of prices in the file. This is because it only reads through the file once and performs a constant number of operations for each price. The space complexity is also O(n) since it stores the list of prices in memory. We could convert the prices file to binary and read it as a memory mapped file using something like `numpy.memmap` if we wanted to reduce the memory usage.


For the bonus question, the `find_triplet` method first reads the file and extracts the items whose price is less than or equal to the gift card balance. Then it loops over all possible triplets of items and checks whether their sum is equal to the balance or less than it. The time complexity of this program is O(n^3). This is because there are three nested loops, each running over n iterations. The space complexity is still O(n), but since we only store the prices less than or equal to the gift card balance, the actual number of items that we need to consider may be much smaller than n.