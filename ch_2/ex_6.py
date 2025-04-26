# Exercise 6
# Ask the user to input three numbers representing a lower limit, a higher limit, and a step value.
#   The program should use a range object to loop through and print the numbers from low to high (inclusive), taking into consideration the step.

#!/usr/bin/env python3
lower = int(input("Lower limit: "))
upper = int(input("Higher limit: "))
step = int(input("Step: "))
for i in range(lower,upper+1,step):
    print(i)
