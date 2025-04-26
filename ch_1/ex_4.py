# Write a program that asks the user to enter a sentence.
#	The program should determine and print the following information:
#		The first character in the string of text and the number of times it occurs in the string.
#		The last character in the string of text and the number of times it occurs in the string.

#!/usr/bin/env python3
text = input("Enter a sentence: ")
first = text[0]
last = text[-1]
f_times = text.count(first)
l_times = text.count(last)
print("The first character \'" + first.upper() + "\' appeared " + str(f_times) + " times")
print("The last character \'" + last.upper() + "\' appeared " + str(l_times) + " times")




