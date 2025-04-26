# Exercise 2
# Rewrite the preceding exercise to additionally print out how many digits are in the number, if the number is an integer.

#!/usr/bin/env python3
num = input("Enter a lucky number: ")
number = int(num)

if num.isdigit():
    count=1
    print("You entered",num)
    while number/10 >= 1:
       number /= 10
       count+=1
    print("The number you entered has",count, "digit(s).")
else:
    print("Please enter an integer.")
