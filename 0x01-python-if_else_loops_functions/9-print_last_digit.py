#!/usr/bin/python3
#print_last_digit-it print last digit
#emmanue <senu.e30@gmail.com>

def print_last_digit(number):
    if number < 0:
        number = -number
    print(number % 10, end="")
    return(number % 10)
