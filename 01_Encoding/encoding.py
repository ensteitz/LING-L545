'''
This is the first file that should be ran in this practical, then checker.py
I made sure to explain my code, so it should be clear. If you have any questions, you can ask me.
'''
import sys
import string

# The possible characters in Sardinian
alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÈÌÒÙÁÉÍÓÚÜÇàèìòùáéíóúüç")

char_freq = {}

def process_line(line):
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
        sys.stdout.write(line)

# Process lines from stdin
for line in sys.stdin:
    process_line(line)


# This part took me forever!
# Should be fixed now
# Sort and output the unknown characters to stdout
unknown_chars = sorted(((freq, char) for char, freq in char_freq.items() if char not in alphabet and char not in string.punctuation), reverse=True)
for freq, char in unknown_chars:
    sys.stderr.write(f"{freq}\t{char}\n")
