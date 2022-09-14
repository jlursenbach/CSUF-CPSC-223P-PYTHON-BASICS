#!/usr/bin/env python3

# Jacob Ursenbach

"""

"""
from math import sqrt


# Python program to check leap year

def is_leap(inp_year) -> bool:
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    else:
        if inp_year % 4 == 0:
            return True

    return False


def is_prime(inp_num: int) -> bool:
    if inp_num < 1:
        return False

    current_check = 2

    while current_check < sqrt(inp_num):

        if inp_num % current_check == 0:
            return False

        current_check += 1

    return True


if __name__ == "__main__":

    for year in range(1990, 2023):
        print(f"{year}: {is_leap(year)}\n")

    for num in range(2, 100):
        print(f"{num}, {is_prime(num)}")

    print((4 ** 3) + 0 + (7 ** 3))
