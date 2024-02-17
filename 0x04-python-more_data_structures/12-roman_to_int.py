#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == "":
        return 0

    my_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num = 0
    for n in range(len(roman_string)):
        if n > 0 and my_dict[roman_string[n]] > my_dict[roman_string[n-1]]:
            num += my_dict[roman_string[n]] - 2 * my_dict[roman_string[n-1]]
        else:
            num += my_dict[roman_string[n]]

    return num
