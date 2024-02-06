#!/usr/bin/python3

""" Module reads from stdin and gets details from it"""


def print_metrics(file_size, status_num):
    """Function that prints metric based on parameter

    Prarameter:
        file_size (int): the size of a file
        status_count (dict): a dict to print out

    Return:
        None
    """
    print("File size: {}".format(file_size))
    for status_code in sorted(status_num.keys()):
        print("{}: {}".format(status_code, status_num[status_code]))


def log_parser():
    """
    Function reads computes metrics and get status code from it

    Parameter:
        None

    Return:
        None
    """
    import sys

    file_size = 0
    counter = 0
    status_num = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                status_code = int(parts[-2])
                file_size += int(parts[-1])
                status_num[status_code] += 1
                counter += 1

                if counter % 10 == 0:
                    print_metrics(file_size, status_num)
            except (ValueError, IndexError):
                continue

    except KeyboardInterrupt as e:
        print_metrics(file_size, status_num)
        print(e)


if __name__ == "__main__":
    log_parser()
