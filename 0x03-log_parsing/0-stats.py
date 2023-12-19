#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics"""

import sys
import signal


def main():
    lines = []
    total_size = 0
    status_count = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            line = line.strip()
            if is_valid_format(line):
                parts = line.split()
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_size += file_size
                status_count[status_code] += 1
                lines.append(line)

                if len(lines) == 10:
                    print_stats(total_size, status_count)
                    lines = []
    except KeyboardInterrupt:
        print_stats(total_size, status_count)


def is_valid_format(line):
    parts = line.split()
    return len(parts) == 10 and parts[5].isdigit() and parts[8].isdigit()


def print_stats(total_size, status_count):
    print(f"Total file size: File size: {total_size}")
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")


if __name__ == "__main__":
    main()
