# Exercise 3
# Write a program that prompts twice for an integer.
#   The program should print the larger of the two numbers.
#   If the numbers are equal, then the program should indicate it as such.

#!/usr/bin/env python3
num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))
if num_1 > num_2:
    print(num_1,"is greater than",num_2)
elif num_1 < num_2:
    print(num_1,"is less than",num_2)
elif num_1 == num_2:
     print(num_1,"is equal to",num_2)


