# Final Project

For my project, I wanted to merge text encoding and segmentation with data scraped from a social media platform.

## Collecting the data:
To begin, I coded "get _ comments.py" to scrape data from this url: 
 - [Link] (https://www.reddit.com/r/IsraelPalestine/comments/172w9gt/i_have_changed_my_mind_about_the_israelpalestine/?sort=new)
 - This outputs the files df\_comments.csv and comments.txt


## Cleaning the data:
From there, I went about cleaning the CSV file. This is done in clean_csv.py.
 - This code removes unnecessary lines from the data such as hyperlinks, AutoModerator comments, and empty lines.
The output is a file called df_clean_comments.csv

In addition to ensuring the coding of the data is correct, I had noticed when scraping that the data that there was a marker in front of sentences that were replies to comments. While this would be great to keep for an in depth analysis surrounding specific conversations, it is not needed for this analysis. Therefore, they have been removed for text cleaning purposes.

The removal of the reply marker '>' at the beginning of sentences was done through through terminal with the following pipeline command:
 - cat comments.txt | sed 's/^>//g' > mod_comments.txt

## Segmenting the data:

In this step, some of the data in the text file was segmented: each sentence is returned on a new line for text analysis by breaking down the comment bodies line per line in a text file.

This was done through the command line:
1. sed '/a-zA-Z/!d' \< mod_comments.txt \> mod2\_comments.txt
2. sed '/\[deleted\]/d' \< mod2_comments.txt \> mod3\_comments.txt
3. sed '/[^https:\/\/.*/d' \< mod3\_comments.txt \> mod4\_comments.txt

## Sentiment Analysis:
Using VADER, sentiment analysis was performed on the text scraped from the original Reddit post.


## Data Visualization
PNGs of data visualization models are included in this folder. The most important ones are the Upvotes vs Compound Sentiment Score, Comments by Time of Day, and Comments by Sentiment Category.
