# Exercise 8
# Write a program that prompts the user twice for a number.
#   The first number will be the base, and the second number will be the exponent.
#       Print the result of raising the base to the exponent.

#!/usr/bin/env python3
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
fmt = "{} raised to power {} is {}"
print(fmt.format(base,exp,base**exp))
