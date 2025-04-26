# Exercise 6
# Rewrite Exercise 4 to count the frequency of each word in the user's input.
#   A dict provides the perfect data structure for this problem.
#       Let the words be the keys, and let the counts be the values.
#   Print the results sorted by the words.
#   Finally, print the results sorted by the counts.

#!/usr/bin/env python3
prompt = "Enter a sentence: "
words_raw = list()
words = list()
words_set = set()
words_dict = dict()
data = input(prompt)
words_raw = data.split(" ")

for word in words_raw:
    word = word.lower()
    words.append(word)
    words_set.add(word)
for word in words:
    if word in words_dict.keys():
        words_dict[word]+=1
    else:
        words_dict[word] = 1
keys_list = list(words_dict.keys())
values_list = list(words_dict.values())
values_list.sort(reverse=True)
print(keys_list)
print(values_list) 
words_set_list = list(words_set)
words_set_list.sort()
#sorted by words
print("#sorted by word (alphabetically)")
keys_list.sort()
fmt = "{0:>8} -- {1}"
for word in keys_list:
    print(fmt.format(word,words_dict[word]))
print()
print("#sorted by word length")
keys_list.sort(key=len)
for word in keys_list:
    print(fmt.format(word,words_dict[word]))
print()
#sorted by count
print("#sorted by word count")
sorted_by_values = dict(sorted(words_dict.items(),key = lambda item: item[1],reverse=True))
for item in sorted_by_values.items():
    print(fmt.format(item[0],item[1]))

# print(words)
# print("Total number of words: ",len(words))
# print()
# print(words_set_list)
# print("Unique words: ",len(words_set))