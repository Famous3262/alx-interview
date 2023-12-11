#!/usr/bin/python3
"""A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file
"""
import math


def minOperations(n):
    if n == 1:
        return 0  # If n is 1, no operations are needed as there is already one H character in the file

    operations = 0
    factor = 2

    while factor * factor <= n:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    if n > 1:
        operations += n

    return operations
