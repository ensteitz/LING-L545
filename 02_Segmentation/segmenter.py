import sys
import re

sent_id = 0

# Define a function to handle ambiguities with punctuation. This formula should include cases of abbreviations in Sardinian
# I did this to account for the following abbreviations: a.D., s.a., t.n.t., s.p.s., b.p., d.m., s.t., f., s.i., m.p., c.p., n.p., s.v., p.i., s.p., ap.C., a.C., publ., n., v., p., cap., fig., tav., vol., pagg.
# There is one abbreviation in particular that, when I tried to add it to the list, it created problems... the abbreviation is "it." , so currently this 
# version of the segmenter cannot recognize that abbreviation. It would be something to revisit in the future.

def split_sentence(sentence):
    # Split the sentence on spaces, but handle punctuation in numerical expressions and abbreviations
    # Updated: 30 April 2024. Should handle most cases...
    return re.findall(r'\b(?:\d[\d,.]*)|(?:[^\W\d_]+\.\s*)*[^\W\d_]+|[^\s\w]', sentence)

def segment(paragraph):
    global sent_id
    result = ""
    # Reset the word_id variable each time so it does not carry over to the next sentence
    word_id = 0
    # Use a reg ex to deal with period ambiguities
    # This should work...
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
    # Read input from encoded_wiki.txt
    with open("encoded_wiki.txt", "r", encoding="utf-8") as encoded:
        wiki = encoded.read()

    # Call the function and get segmented text
    segmented_text = segment(wiki)

    # Write results to segmented_wiki.txt
    with open("segmented_wiki.txt", "w", encoding="utf-8") as segmented:
        segmented.write(segmented_text)
    print(f"The file {encoded} has been segmented. The results have been saved in {segmented}")
