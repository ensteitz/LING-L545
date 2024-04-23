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
sa = open("reddit_body.txt", "r")

# Create a variable to store the text of the reddit post (comments and replies)
sa_write = open("reddit_body_sa.txt", "w")

sentence = sa.readlines()

# Iterate over the sentences in the text file, creating polarity scores for each using the polarity_scores() method to collect polarity measures
for line in sentence:
	print(line, file=sa_write)	# Sstore the output in a file that contains only the sentences and their polarities
	print(analyser.polarity_scores(line), file=sa_write)
	print("------------\n", file=sa_write)


df = pd.read_csv('cip_PRAWreddit.csv')
print("step 1")
df = df.loc[:,['timestamp','body']]

sid_obj = SentimentIntensityAnalyzer()

# Function to pre-precess
def preprocess_data(df):
	df["body"] = df["body"].apply(lambda x:x.translate(str.maketrans('','',string.punctuation)))
	df["timestamp"] = pd.to_datetime(df["timestamp"])
	df["month"] = df['timestamp'].dt.strftime('%b')
	return df

# Compute sentiment and plot monthly score
def sentiment(df):
	sentiment_scores = []
	for text in df['body']:
		scores = sid_obj.polarity_scores(text)
		sentiment_scores.append(scores['compound'])
	df['sentiment_score'] = sentiment_scores

	# Group by month and compute the mean sentiment score
	monthly_avg_sentiment = df.groupby('month')['sentiment_score'].mean().reset_index()

	# Initialize a DataFrame with all months
	all_months = pd.DataFrame({'month': pd.date_range(start='2023-10-07', end='2023-10-31', freq='MS').strftime('%b')})

	# Merge sentiment data with all months
	monthly_avg_sentiment = all_months.merge(monthly_avg_sentiment, on='month', how='left')

	# Replace NaN values with 0
	monthly_avg_sentiment['sentiment_score'] = monthly_avg_sentiment['sentiment_score'].fillna(0)

	sns.set_style('whitegrid')
	sns.barplot(x='month', y='sentiment_score', data=monthly_avg_sentiment)

df = preprocess_data(df)
sentiment(df)
