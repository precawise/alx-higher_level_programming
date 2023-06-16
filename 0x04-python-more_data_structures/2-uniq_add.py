#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_set = set(my_list)
    sum_result = 0
    for element in unique_set:
        sum_result += element
    return sum_result
