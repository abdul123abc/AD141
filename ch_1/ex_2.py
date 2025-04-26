##Exercise 2
# Write a program that prompts twice for text from the user.
# 	The first input should be a first name.
# 	The second input should be a last name.
# 	The program should print the full name on one line and the person's initials on the second line.

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
fullname = fname.capitalize() +" "+ lname.capitalize()
print(fullname, fname[0].upper() ,".", lname[0].upper(),sep = " ")
