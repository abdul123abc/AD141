# Exercise 7
# Write a program that prompts the user for a string and then prompts again for a number.
#   The program should create and print a new string by using the repetition operator on the string and the number.
#       For example, if the string is hello and the number is 3, then hellohellohello should be printed.

#!/usr/bin/env python3
word = input("Enter a word: ")
num = int(input("Enter a number: "))
print("word" * num)
