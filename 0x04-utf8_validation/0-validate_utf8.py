#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """ Count the number of leading 1s in the first byte"""
    num_bytes = 0
    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask = mask >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num & (1 << 7) and not (num & (1 << 6))):
                return False
        num_bytes -= 1
    return num_bytes == 0
