# Final Project

For my project, I wanted to merge text encoding and segmentation with data scraped from a social media platform.

## Collecting the data:
To begin, I imported the libraries scraped data from a particular post on Reddit and stored the text in a file named comments_txt.

## Cleaning the data:
Next, I created code to remove unnecessary lines from the data. This code is in clean_csv.py .

In addition to ensuring the coding of the data is correct, I had noticed when scraping that the data that there was a marker in front of sentences that were replies to comments. While this would be great to keep for an in depth analysis surrounding specific conversations, it is not needed for this analysis. Therefore, they have been removed for text cleaning purposes.

## Segmenting the data:
In this step, the data is segmented: each sentence is returned on a new line for text analysis. By breaking down the sentences line per line

## Sentiment Analysis:
Using VADER, sentiment analysis was performed on the text scraped from the original Reddit post.
