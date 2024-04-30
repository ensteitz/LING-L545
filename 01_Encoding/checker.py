'''
This file should be run SECOND for this practical.
It takes the result of encoding.py ('verified_alphabet_wiki.txt') and then checks to make sure everything is encoded in UTF-8.
It also fixes any problems with spacing characters.
The result is a file called 'encoded_wiki.txt'

I made sure to socument the steps well, so it should be very easy to follow.
'''

import sys
import re

def is_utf8_encoded(wiki):
    try:
        with open(wiki, 'r', encoding='utf-8') as file:
            file.read()
        return True
    except UnicodeDecodeError:
        return False

def replace_unicode_chars(word):
    # Check to see if there are any alternate spaces
    for char in chars_to_replace:
        if char in word:
            # Change the encoding if so to good ol' U+0020
            word = word.replace(char, "\u0020")
    return word

def fix_encoding(wiki, encoded):
    # Define new function to perform action on opened file, very convenient
    with open(wiki, 'r', encoding='utf-8') as file:
        words = file.read().split()

    # Process each word and replace Unicode characters if found
    uniform_encoding = [replace_unicode_chars(word) for word in words]

    # Don't forget to save the words back in the file
    with open(encoded, 'w', encoding='utf-8') as file:
        file.write(' '.join(uniform_encoding))

wiki = 'verified_alphabet_wiki.txt'
encoded = 'encoded_wiki.txt'

chars_to_replace = [
    "\u00A0", "\u1680", "\u2000", "\u2001", "\u2002",
    "\u2003", "\u2004", "\u2005", "\u2006", "\u2007",
    "\u2008", "\u2009", "\u200A", "\u202F", "\u205F",
    "\u3000"
]


# Just a quick check to ensure proper encoding before trying to process the other functions
if is_utf8_encoded(wiki):
    print(f"{wiki} is encoded in UTF-8.")
else:
    print(f"{wiki} is not encoded in UTF-8.")

# Process the functions and hopefully get a result
# Not getting a result.......... grr
# Fix later
fix_encoding(wiki, encoded)
print(f"Unicode characters replaced successfully in {encoded}.")
