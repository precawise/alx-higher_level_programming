#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_num = 0
    for a in range(real_num, x):
        try:
            print("{:d}".format(my_list[a]), end='')
            real_num += 1
        except (ValueError, TypeError):
            pass
    print()
    return real_num
