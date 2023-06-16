#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    multiplied_list = [x * number for x in my_list]
    return multiplied_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list.copy(), 4)
    print(new_list)
    print(my_list)
