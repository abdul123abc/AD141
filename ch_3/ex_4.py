# Exercise 4
# Use a single set to determine the number of unique words in the user's input.
#   You can use the same sample while loop from Exercise 1.
#       Each time through the loop, the individual words should be added to the single set.
#   When done looping, output the contents of the set sorted alphabetically.
#   Also, output the number of unique words.

#!/usr/bin/env python3
prompt = "Enter a sentence: "
words_raw = list()
words = list()
words_set = set()

data = input(prompt)
words_raw = data.split(" ")

for word in words_raw:
    word = word.lower()
    words.append(word)
    words_set.add(word)
words_set_list = list(words_set)
words_set_list.sort()
print(words)
print("Total number of words: ",len(words))
print()
print(words_set_list)
print("Unique words: ",len(words_set))
