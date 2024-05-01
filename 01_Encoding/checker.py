'''
This file should be run SECOND for this practical.
'''

import sys
import re

def is_utf8_encoded(text):
    try:
        # Encode the text using utf-8 to check if it's properly encoded
        text.encode('utf-8')
        return True
        # Add this to catch errors. It should work now...
    except UnicodeEncodeError:
        return False

def replace_unicode_chars(text, chars_to_replace):
    # Check to see if the content contains any of the Unicode characters to be replaced
    for char in chars_to_replace:
        if char in text:
            # Change the encoding to the standard space character U+0020
            text = text.replace(char, "\u0020")
    return text

def fix_encoding(text, chars_to_replace):
    # Process each word and replace Unicode characters, if any were found
    modified_text = replace_unicode_chars(text, chars_to_replace)

    # Print the text with encoding transformations
    sys.stdout.write(modified_text)

wiki_text = sys.stdin.read()

chars_to_replace = [
    "\u00A0", "\u1680", "\u2000", "\u2001", "\u2002",
    "\u2003", "\u2004", "\u2005", "\u2006", "\u2007",
    "\u2008", "\u2009", "\u200A", "\u202F", "\u205F",
    "\u3000"]

# Just a quick check to ensure proper encoding before trying to process the other functions
wiki = 'verified_alphabet_wiki.txt'
encoded = 'encoded_wiki.txt'

if is_utf8_encoded(wiki_text):
    print(f"{wiki} is encoded in UTF-8.")
else:
    print(f"{wiki} is not encoded in UTF-8.")

# Process the functions and save the result in the output file
fix_encoding(wiki_text, chars_to_replace)
print(f"Unicode characters replaced successfully in {encoded}.")
