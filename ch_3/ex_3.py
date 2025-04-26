# Exercise 3
# Write a program that creates a loop asking the user to input a number.
#   Repeat this process until the user enters the value end.
#   Enter each number into a set.
#       Before you enter the number, verify if the number is already in the set.
#       If the number is already in the set, then update a counter that tracks how many entries are not added to the set.
#   Just before the program ends, print the following:
#       The contents of the set on one line
#       The number of elements that were NOT added to the set on the second line

#!/usr/bin/env python3
prompt = "Enter a number (or the word 'end' to quit): "
nums = set()
dup = list()
count = 0
while True:
    data = input(prompt)
    if data.isdigit():
        num = int(data)
    if data == "end":
        break
    if num not in nums:
        nums.add(num)
    elif num in nums:
        print("\t", num, "already exists and is ignored")
        count+=1
        dup.append(num)
        continue
print("Numbers: ",nums)
print("Numbers not added: ",dup)
print("Count of numbers not added: ",count)