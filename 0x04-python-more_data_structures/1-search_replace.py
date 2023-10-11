#!/usr/bin/python3


def search_replace(my_list, search, replace):
    return list(map(lambda x: replace if search == x else x, my_list))


if __name__ == "__main__":
    search_replace(my_list, search, replace)
