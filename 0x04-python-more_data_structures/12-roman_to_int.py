#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    previous_value = 0

    for char in roman_string:
        current_value = roman_dict.get(char, 0)

        if current_value > previous_value:
            result += current_value - 2 * previous_value
        else:
            result += current_value

        previous_value = current_value

    return result
