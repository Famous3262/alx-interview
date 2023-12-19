#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics"""

import sys
import signal


def signal_handler(signal, frame):
    print_stats()


def print_stats():
    global total_size, status_codes
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


total_size = 0
status_codes = {}

# Set up the signal handler to catch CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        data = line.split()
        # Check if the input line matches the expected format
        if len(data) == 10 and data[8].isdigit():
            total_size += int(data[8])
            status_code = data[9]
            # Check if the status code is valid and update the count
            if status_code in ['200', '301', '400', '401',
                               '403', '404', '405', '500']:
                status_codes[status_code] = status_codes.get(status_code, 0)+1
        """" Print statistics and reset values
        after every 10 lines or keyboard interruption
        """
        if len(status_codes) == 8 or len(status_codes) == 0:
            print_stats()
            total_size = 0
            status_codes = {}
except KeyboardInterrupt:
    print_stats()
