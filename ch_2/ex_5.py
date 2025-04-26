# Exercise 5
# Ask the user to input multiple numbers on one input line.
#   Split the numbers into a list.
#   Write a loop that examines each element of the list and displays the ones that are greater than zero.

#!/usr/bin/env python3
nums = input("Enter multiple numbers: ")
num_list = nums.split()
for i in num_list:
    if int(i) > 0:
        print(i)
