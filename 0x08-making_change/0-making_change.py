#!/usr/bin/python3

def makeChange(coins, total):
    coins.sort(reverse=True)
    i = 0
    numOfCoins = 0
    while i < len(coins):
        if total > 0:
            if coins[i] <= total:
                total -= coins[i]
                numOfCoins += 1
            else:
                i += 1
        elif total < 0:
            return 0
        else:
            return numOfCoins
    return -1