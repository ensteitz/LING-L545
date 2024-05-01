# Encoding Practical:

## Instructions:
1. In order to use this code, please run the file encoding.py through the command line:

    `cat wiki.txt | python3 encoding.py`


   This will result in the text outputting to stdout. Optionally, as I did, you can save the results in a file called verified\_alphabet\_wiki.txt through the following line of code:


    `cat wiki.txt | python3 encoding.py > verified_alphabet_wiki.txt`


   Lastly, to save this code to stderr, use the following line of code ion the command line:


    `cat wiki.txt | python3 encoding.py > verified_alphabet_wiki.txt 2> wiki.valid`


2. Next, I made a python file to check the encoding of whitespaces. This is seen in checker.py . To run this code, use the following in terminal:

    `cat verified_alphabet_wiki.txt | python3 checker.py > encoded_wiki.txt`

   The result should store the content of checker.py in the file encoded\_wiki.txt. To check if it worked, please run the following in terminal:

    `cat encoded_wiki.txt`
