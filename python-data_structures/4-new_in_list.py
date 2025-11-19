#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < len(my_list) and idx >= 0:
        my_list[idx] = element
        return my_list
    return new_list
