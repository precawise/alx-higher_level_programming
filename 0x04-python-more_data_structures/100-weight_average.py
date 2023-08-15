#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight = 0
    total_score = 0

    for tup in my_list:
        score, weight = tup
        total_weight += weight
        total_score += score * weight

    if total_weight == 0:
        return 0

    average = total_score / total_weight
    return float(average)
