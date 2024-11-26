#!/usr/bin/python3


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    numOfCoins = 0
    for i in coins:
        while i <= total:
            total -= i
            numOfCoins += 1
    return numOfCoins if total == 0 else -1
