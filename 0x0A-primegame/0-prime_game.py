#!/usr/bin/python3
""" Prime game """


def isWinner(x, nums):
    """ finding the winner"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def next_prime(num):
        num += 1
        while not is_prime(num):
            num += 1
        return num

    def can_win(n):
        if n % 2 == 0:
            return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Example usage
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))
