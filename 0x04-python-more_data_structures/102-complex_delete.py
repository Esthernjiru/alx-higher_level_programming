#!/usr/bin/python3
#102-complex_delete.py

def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for k, v in tmp.items():
        if value == v:
            my_dict.pop(k)
    return my_dic

