#!/usr/bin/python3

def modify_list(original_list, search_value, replacement_value):
    modified_list = []
    for item in original_list:
        if item == search_value:
            modified_list.append(replacement_value)
        else:
            modified_list.append(item)
    return modified_list
