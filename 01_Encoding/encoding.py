import sys
import string

# The possible characters in Sardinian
alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÈÌÒÙÁÉÍÓÚÜÇàèìòùáéíóúüç")

char_freq = {}

def process_line(line):
    # In case of error
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
        print(line.strip())

# Open the file in this file. Could have used it as sys.stdin, but I find this easier
with open("wiki_copy.txt", "r") as f:
    for line in f:
        process_line(line)

# This part took me forever!
# Should be fixed now
# Not only will the results be stored in wiki.valid, but it will also be sorted thanks to the string library
unknown_chars = sorted(((freq, char) for char, freq in char_freq.items() if char not in alphabet and char not in string.punctuation), reverse=True)

# Now export the buggers
with open("wiki.valid", "w") as output_file:
    for freq, char in unknown_chars:
        output_file.write(f"{freq}\t{char}\n")
