# Exercise 4
# Write a program that prompts twice for an integer.
#   The program should output the sum of the integers within the range of those two numbers inclusively
#    For example, if the user inputs the numbers 10 and 15, then the sum would be 75.
#           10 + 11 + 12 + 13 + 14 + 15 = 75

#!/usr/bin/env python3
start = int(input("Start: "))
end = int(input("End: "))
total = 0
for i in range(start,end+1):
    total += i
print("The sum of munbers between",start,"and",end,"is",total)
