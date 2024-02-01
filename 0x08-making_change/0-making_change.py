#!/usr/bin/python3
"""Determining the fewest number of coins needed to meet
a given amount total at a given pile of coins of different values
"""
import sys


def makeChange(coins, total):
    """ Return: fewest number of coins needed to meet total
                If total is 0 or less, return 0
                If total cannot be met by any number
                of coins you have, return -1
    """
    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    table = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        table += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return table
