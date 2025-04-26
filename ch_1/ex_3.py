#Exercise 3
#    	Write a program that accepts a string from the user.
# 	Determine and print the following information about the string:
#	 	Does it end in a period?
# 		Does it contain all alphabetic characters?
# 		Is there an 'x' in the string?
#	Create and print a new string that has all occurrences of e changed to E.

#!/usr/bin/env python3
text = input("Enter a string of words: ")
print("Ends with period? " + str(text.endswith(".")))
print("Contains all alphabetic characters? " + str(text.strip().isalpha()))
char = "x"
print("Contains an \"X\"? " + str(text.find(char)))
new_text = text.replace("e","E")
print(new_text)
