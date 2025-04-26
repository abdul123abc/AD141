# Exercise 1
# Write a program that prompts for a lucky number. The program should print out a message if the number entered is not an integer.

#!/usr/bin/env python3
num = input("Enter a lucky number: ")
if num.isdigit(): 
    print("You entered ",num)
else:
    print("Please enter an integer.")
