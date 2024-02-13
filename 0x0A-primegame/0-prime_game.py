#!/usr/bin/python3
""" Prime game """


def isWinner(x, nums):
    """find winner"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def next_prime(num):
        num += 1
        while not is_prime(num):
            num += 1
        return num

    def winner(n):
        if n % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = []
    for n in nums:
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p = next_prime(p)

        count_primes = sum(primes)
        winners.append(winner(count_primes))

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
