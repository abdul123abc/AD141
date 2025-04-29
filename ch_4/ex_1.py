# Exercise 1
# Write and test a function that is designed to validate input.
#   The function should prompt the user for a positive integer.
#   It should validate the information entered by the user is indeed a positive integer.
#       If number entered is valid, the function should return the number.
#       If the number entered is invalid, the function should return a zero (0) instead.
#    The application, not the function, should indicate with a message in the output each time an invalid entry is given.

#!/usr/bin/env python3

def positive_int(num):
    prompt = "Enter a positive integer: "
    num = int(input(prompt))
    if num > 0:
        return num
    else:
        return 0
number = 1
if positive_int(number) == 0:
    print("Invalid Entry")

