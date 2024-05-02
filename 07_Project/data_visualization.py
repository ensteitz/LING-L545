import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ast

plt.rcParams['lines.markersize'] = 2

# Load the CSV file into a data frame
df = pd.read_csv("df_sa_extralabels_clean_comments.csv")

# Convert the string representation of sentiment scores to dictionaries
df["sentiment_scores"] = df["sentiment_scores"].apply(ast.literal_eval)

# Create a new column "compound_score" by taking out the "compound" value from "sentiment_scores"
df["compound_score"] = df["sentiment_scores"].apply(lambda x: x["compound"])

# Turn scores into strings and save to df
def categorize_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment_category'] = df['compound_score'].apply(lambda x: categorize_sentiment(x))

df.to_csv("df_sa_extra_extralabels_clean_comments.csv", index=False)

print(df)

# Data exploration for fun. To check out what it looks like rn
print(df.head())  # Check the first few rows of the DataFrame
print(df.info())  # Get information about the DataFrame

# Data visualization!!

# 1. Bar Plot: Number of Comments by Time of Day
time_of_day_order = ["Early Morning", "Morning", "Afternoon", "Evening", "Night"]
# Since the data was taken over a 24-hour window,
# These times were chosen to get a better picture of the 24 hour time frame
plt.figure(figsize=(10, 8))
sns.countplot(x='time_of_day', data=df, order=time_of_day_order)
plt.title('Number of Comments by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Number of Comments')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.savefig('comments_by_time_of_day.png')
plt.close()


# 2. Histogram: Distribution of Upvotes
sns.histplot(df['upvotes'], bins=20)
plt.title('Distribution of Upvotes')
plt.xlabel('Upvotes')
plt.xlim(-20, 25)
plt.ylabel('Frequency')
plt.savefig('upvotes_distribution.png')
plt.close()
# This one needs work...won't be used in the paper

# 2.5 Box Plot
sns.boxplot(x='upvotes', data=df)
plt.title('Distribution of Upvotes')
plt.xlabel('Upvotes')
plt.xlim(-10, 15)
plt.savefig('upvotes_boxplot.png')
plt.close()
# This one could be beteter

# 3. Box Plot: Upvotes by Time of Day
sns.boxplot(x='time_of_day', y='upvotes', data=df)
plt.title('Upvotes by Time of Day')
plt.xlabel('Time of Day')
plt.ylim(-10, 25)
plt.ylabel('Upvotes')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.savefig('upvotes_by_time_of_day.png')
plt.close()
# Good

# 4. Scatter Plot: Upvotes vs. Compound Sentiment Scores
sns.scatterplot(x='compound_score', y='upvotes', data=df)
plt.title('Upvotes vs. Compound Sentiment Score')
plt.xlabel('Compound Sentiment Scores')
plt.xlim(-1, 1)
plt.ylabel('Upvotes')
plt.ylim(-15, 20)
plt.savefig('upvotes_vs_compound_sentiment_score.png')
plt.close()


# 5. Bar Plot of Sentiment Category
sns.countplot(x='sentiment_category', data=df)
plt.title('Number of Comments by Sentiment Category')
plt.xlabel('Sentiment Category')
plt.ylabel('Number of Comments')
plt.savefig('comments_by_sentiment_category.png')
plt.close()


# Some of these are wonky still... I just wanted to play around with data visualization.

# Sentiment counts for the 'sentiment_category'
sentiment_counts = df['sentiment_category'].value_counts()
print(sentiment_counts)

# The result should be a table with the sentiment counts
