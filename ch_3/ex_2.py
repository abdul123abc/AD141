# Exercise 2
# Write a program that creates a loop asking the user to input a number.
#   Repeat this process until the user enters the value end.
#       The following can be used to loop through the user input.
#           prompt = "Enter a number (or the word 'end' to quit) "
#           while True:
#               data = input(prompt)
#               if data == "end":
#                   break
#               #Remainder of while loop goes here
#   Add each iteration number to a list.
#   Just before the program ends, print the following:
#       The contents of the list on one line 
#       The sum of the elements in the list on the second line

#!/usr/bin/env python3
prompt = "Enter a number (or the word 'end' to quit): "
nums = list()
while True:
    data = input(prompt)
    if data == "end":
        break
    nums.append(int(data))
print("Numbers: ",nums)
sum = 0
for i in nums:
    sum+=i
print("Sum of all numbers: ",sum)
