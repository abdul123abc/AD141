# Exercise 6
# Write a program that prompts twice for an integer.
#   Print the product of the two numbers.
#   Once this works properly, try entering numbers with a decimal point.
#       What happens? Why?
#   Now try entering data that is nonnumerical.
#       What happens? Why?

#!/usr/bin/env python3
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
product = num_1 * num_2
fmt = "{} x {}  = {}" 
print(fmt.format(num_1,num_2,product))
