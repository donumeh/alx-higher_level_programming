#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []

    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ValueError:
            print("value error")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
        i += 1
    return new_list
