# Exercise 2
# Write and test a function that takes a collection of strings and returns the length of the longest string in the collection.
#   The application should loop through the collection of strings and rely on the value returned by the 
#   function to format all of the strings to the output such that they are all right justified to the width of the longest string.

#!/usr/bin/env python3
def longest(string):
    long = ""
    for i in string:
        print(i,end = '\n')
string = input("Enter multiple strings: ")
string = string.strip().split(" ")
string_1 = ["I","am","very","good"]
longest(string)
print()
longest(string_1)

