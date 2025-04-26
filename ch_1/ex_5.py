# Exercise 5
# Write an application that prompts to enter the radius of a circle.
#   Accept the user input into a variable.
#   Compute and print the area of the circle whose radius was input.
#       The formula for the area of a circle is πr² (pi times the square of the radius).
#       Use 3.14159 for pi.

#!/usr/bin/env python3
pi = 3.14159
radius = int(input("Enter the radius of the circle in cm: "))
area = pi * (radius**2)
print("The area ot the circle is " +  str(area))
