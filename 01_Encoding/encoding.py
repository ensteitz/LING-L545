'''
This is the first file that should be ran in this practical, then checker.py
I made sure to explain my code, so it should be clear. If you have any questions, you can ask me.
'''

import sys
import string

# The possible characters in Sardinian
alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÈÌÒÙÁÉÍÓÚÜÇàèìòùáéíóúüç")

char_freq = {}

def process_line(line, destination):
    valid_line = False

    for char in line:
        if char in alphabet or char in string.punctuation:
            valid_line = True
            # Freq of known characters
            char_freq[char] = char_freq.get(char, 0) + 1
        else:
            # Freq of unknown characters
            char_freq[char] = char_freq.get(char, 0) + 1

    # Print the line ONLY IF it contains valid characters
    if valid_line:
        destination.write(line)

# Open the file in this file. Could have used it as sys.stdin, but I find this easier
with open("wiki.txt", "r") as source, open("verified_alphabet_wiki.txt", "w") as destination:
    for line in source:
        process_line(line, destination)


# This part took me forever!
# Should be fixed now
# Not only will the results be stored in wiki.valid, but it will also be sorted thanks to the string library
unknown_chars = sorted(((freq, char) for char, freq in char_freq.items() if char not in alphabet and char not in string.punctuation), reverse=True)

# Now export the buggers
with open("wiki.valid", "w") as f_unknown_chars:
    for freq, char in unknown_chars:
        f_unknown_chars.write(f"{freq}\t{char}\n")
