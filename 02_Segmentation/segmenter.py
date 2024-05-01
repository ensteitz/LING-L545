import re
import sys

sent_id = 0

def split_sentence(sentence):
    # Split the sentence on spaces, but handle punctuation in numerical expressions and abbreviations
    return re.findall(r'\b(?:\d[\d,.]*)|(?:[^\W\d_]+\.\s*)*[^\W\d_]+|[^\s\w]', sentence)

def process_paragraph(paragraph):
    global sent_id
    result = ""
    # Initialize word_id counter outside the loop
    word_id = 0
    # Use a regular expression to handle periods within quotes as part of the sentence
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph)
    for sentence in sentences:
        if sentence.strip() == '':
            continue
        sent_id += 1
        # Reset word_id to 0 at the beginning of each sentence
        word_id = 0
        result += f'# sent_id = {sent_id}\n'
        result += f'# text = {sentence.strip()}\n'
        words = split_sentence(sentence)
        for word in words:
            if word.strip() != '':
                word_id += 1
                result += f'{word_id}\t{word}\t_\t_\t_\t_\t_\t_\t_\t_\n'
        result += '\n'
    return result

if __name__ == "__main__":
    # Read input from standard input
    input_text = sys.stdin.read()

    # Process the input and get segmented text
    segmented_text = process_paragraph(input_text)

    # Print segmented output to standard output
    print(segmented_text)
