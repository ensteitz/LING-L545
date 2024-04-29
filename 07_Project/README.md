# Final Project

For my project, I wanted to merge text encoding and segmentation with data scraped from a social media platform.

## Collecting the data:
To begin, I coded "get _ comments.py" to scrape data from this url: 
 - https://www.reddit.com/r/IsraelPalestine/comments/172w9gt/i_have_changed_my_mind_about_the_israelpalestine/?sort=new
 - this outputs the files df_comments.csv


## Cleaning the data:
From there, I went about cleaning the CSV file. This is done in clean_csv.py
 - this outputs the file '''df_clean_comments.csv'''
 - this code removes unnecessary lines from the data such as hyperlinks, AutoModerator comments, and empty lines.
The output is a file called df_clean_comments.csv

In addition to ensuring the coding of the data is correct, I had noticed when scraping that the data that there was a marker in front of sentences that were replies to comments. While this would be great to keep for an in depth analysis surrounding specific conversations, it is not needed for this analysis. Therefore, they have been removed for text cleaning purposes.

## Segmenting the data:

In this step, some of the data was segmented: each sentence is returned on a new line for text analysis. By breaking down the comment bodies line per line in a text file.

The text file is 

## Sentiment Analysis:
Using VADER, sentiment analysis was performed on the text scraped from the original Reddit post.
