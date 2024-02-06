#!/usr/bin/python3

""" Module reads from stdin and gets details from it"""


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
    status_num = {200: 0, 301: 0, 400: 0, 401: 0, 404: 0, 405: 0, 500: 0}

    for line in sys.stdin:
        status_code = int(line.split(" ")[-2])
        file_size += int(line.split(" ")[-1])

        if status_code in status_num:
            status_num[status_code] += 1

        if counter == 10:
            print("File size: {}".format(file_size))

            for key, value in status_num.items():
                if value <= 0:
                    continue
                print("{}: {}".format(key, value))
                status_num[key] = 0

            counter = 0

        counter += 1


if __name__ == "__main__":
    log_parser()
