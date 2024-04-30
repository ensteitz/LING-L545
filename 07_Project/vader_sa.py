# VADER sentiment analysis
# Before running this, make sure to pip install vaderSentiment, matplotlib, and seaborn
# If you don't already have vader, install that too

import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import string
import datetime
import seaborn as sns
import matplotlib as plt

analyser = SentimentIntensityAnalyzer()

txt = open("clean_comments.txt", "r")

# Create a variable to store the text of the reddit post (comments and replies) for the individual sentences (not per users' post)
txt_write = open("sa_clean_comments.txt", "w")

sentence = txt.readlines()

# Iterate over the sentences in the text file, creating polarity scores for each using the polarity_scores() method to collect polarity measures
for line in sentence:
        # Store the output in a file that contains only the sentences and their polarities
	print(line, file=txt_write)
	print(analyser.polarity_scores(line), file=txt_write)
        # Do this so that it is easier to see each sentence
	print("------------\n", file=txt_write)

analyser = SentimentIntensityAnalyzer()

# Load the CSV file into a data frame (Pandas)
df = pd.read_csv("df_extralabels_clean_comments.csv")

# Perform sentiment analysis of the text in the "body" column of the data frame and store the results in a new column called "sentiment_scores"
df["sentiment_scores"] = df["body"].apply(lambda x: analyser.polarity_scores(x))

# Save the data frame to a new CSV file
df.to_csv("df_sa_extralabels_clean_comments.csv", index=False)

print(df)

# To help keep track of all the files I'm creating and what is a result of which python file
print("Sentiment analysis results saved to 'df_sa_extralabels_clean_comments.csv'")
