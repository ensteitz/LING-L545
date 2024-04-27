# VADER sentiment analysis
# Installation (Command Prompt (PC) or Terminal (Mac):
# before running this, make sure to pip install vaderSentiment, matplotlib 
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import string
import datetime
import seaborn as sns
import matplotlib as plt

analyser = SentimentIntensityAnalyzer()


# Create a variable to use to open the file with the sentences for sentiment analysis
txt = open("clean_comments.txt", "r")

# Create a variable to store the text of the reddit post (comments and replies) for the individual sentences (not per users' post)
txt_write = open("sa_clean_comments.txt", "w")

sentence = txt.readlines()

# Iterate over the sentences in the text file, creating polarity scores for each using the polarity_scores() method to collect polarity measures
for line in sentence:
	print(line, file=txt_write)	# Sstore the output in a file that contains only the sentences and their polarities
	print(analyser.polarity_scores(line), file=txt_write)
	print("------------\n", file=txt_write)

analyser = SentimentIntensityAnalyzer()

# Load the CSV file into a DataFrame
df = pd.read_csv("df_extralabels_clean_comments.csv")

# Perform sentiment analysis and store the results in a new column called "sentiment_scores"
df["sentiment_scores"] = df["body"].apply(lambda x: analyser.polarity_scores(x))

# Save the DataFrame to a new CSV file
df.to_csv("df_sa_extralabels_clean_comments.csv", index=False)

print(df)

print("Sentiment analysis results saved to 'df_sa_extralabels_clean_comments.csv'")




