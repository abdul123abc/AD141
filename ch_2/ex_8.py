# Exercise 8
# Rewrite exercise # 4 such that the program takes into account the case where the first number entered is bigger than the last.
#   For example, if the user inputs the numbers 10 and 15, then the sum would be 75.
#       10 + 11 + 12 + 13 + 14 + 15 = 75
#   If the user inputs the numbers 15 and 10, then the sum would be still be 75.

#!/usr/bin/env python3
start = int(input("Start: "))
end = int(input("End: "))
total = 0
swap = 0
if start > end:
    swap = start
    start = end
    end = swap
for i in range(start,end+1):
    total += i
print("The sum of munbers between",start,"and",end,"is",total)

