#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_string = roman_string.upper()
    roman_map = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    total = 0
    i = 0

    while i < len(roman_string):
        # next value is larger → subtract
        if (
            i + 1 < len(roman_string)
            and roman_map.get(roman_string[i], 0)
            < roman_map.get(roman_string[i + 1], 0)
        ):
            total += (
                roman_map[roman_string[i + 1]]
                - roman_map[roman_string[i]]
            )
            i += 2
        else:
            total += roman_map.get(roman_string[i], 0)
            i += 1

    return total
