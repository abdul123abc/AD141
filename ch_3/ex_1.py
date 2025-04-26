# Exercise 1
# Given the following two lists:
#   first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
#   second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
#       Concatenate the two lists by index into a new list that, when printed, looks as follows:
#           ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#!/usr/bin/env python3
first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
days = list()
for i in range(len(first)):
    days.append(first[i] + second[i])
print(days)
