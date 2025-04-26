# Exercise 5
# Use a dictionary to create a mapping from the digits 0-9 to the words zero, one, two, etc.
#   Next, ask the user to input a number.
#   If the user enters 1437, then the program should print one four three seven.

#!/usr/bin/env python3
numbers = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
prompt = "Enter a number: "
num = input(prompt)
digits = []
for i in num:
    digits.append(i)
for digit in digits:
    print(numbers[digit],end = '\t')
print()
print(num)
print(digits)