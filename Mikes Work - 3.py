"""
Intermediate Problem: Create a functions reads a file's contents
    and creates a dictionary where each key is a unique word
    and the value is the number of occurrences.

File Name: unique_word_count.py
Name:      ?
Course:    CPTR 141
"""


# Your code goes here
def unique_word_count(filename):
    word_dict = {}
    with open(filename, "r") as file:
        rows = file.read().splitlines()

    for i, r in enumerate(rows):
        rows[i] = r.replace(",", "").replace(".","").lower()
        string_list = rows[i].split(" ")
        for s in string_list:
            if (s == ""):
                string_list.remove(s)
        rows[i] = " ".join(string_list)


    for r in rows:
        string_list = r.split(" ")
        for s in string_list:
            if (s not in word_dict.keys()):
                word_dict[s] = 1
            else:
                word_dict[s] += 1
    return word_dict