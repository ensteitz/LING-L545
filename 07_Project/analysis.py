import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


comments = pd.read_csv("df_clean_comments.csv", parse_dates=["timestamp"])

# Gives you the chart so you can see what it looks like now
print(comments.head())
print('\n')

# How many unique comments are there. could be multiple from same person, so this checks
print(comments.parent_id.unique())
print('\n')

# See the dates the comments were posted
print("This are the times that the comments were posted:")
print(comments["timestamp"])
print('\n')

# When was the first and last comment posted
print("The first comment was posted on:")
print(comments["timestamp"].min())
print('\n')

print("The last comment was posted on:")
print(comments["timestamp"].max())
print('\n')

# How much time passed between the first and last comments
print("This is how much time passed between the first and last comments:")
print(comments["timestamp"].max() - comments["timestamp"].min())
print('\n')

# Find out most upvoted and downvoted comments for fun
print('The most upvoted and downvoted counts:')
print(comments["upvotes"].max())
print(comments["upvotes"].min())
print('\n')

# Add the hour column to the data frame
comments["hour"] = comments["timestamp"].dt.hour

# Define a variable to turn the hours the comments were posted into a time of day
def categorize_time_of_day(hour):
    if hour < 6:
        return "Early Morning"
    elif 6 <= hour < 11:
        return "Morning"
    elif 11 <= hour < 15:
        return "Afternoon"
    elif 15 <= hour < 20:
        return "Evening"
    else:
        return "Night"

# Call the variable and add it to the CSV
comments["time_of_day"] = comments["hour"].apply(categorize_time_of_day)
print(comments.head())
print('\n')

# Specify a new file path to store the results of these new columns
new_CSV = "df_extralabels_clean_comments.csv"

# Save the data frame to a new CSV file
comments.to_csv(new_CSV, index=False)

print(f"New data frame saved to '{new_CSV}'")


# Create a column in the CSV that contains the compound sentiment analysis score for each comment and reply
sid_obj = SentimentIntensityAnalyzer()

def sentiment(comments):
    sentiment_scores = []
    for text in comments['body']:
        scores = sid_obj.polarity_scores(text)
        sentiment_scores.append(scores['compound'])
    comments['sentiment_score'] = sentiment_scores

    # Group by hour and compute the mean sentiment score
    hourly_avg_sentiment = comments.groupby('hour')['sentiment_score'].mean().reset_index()

    # Initialize a data frame with all hours
    all_hours = pd.DataFrame({'hour': pd.date_range(start='2023-10-08 06:00:00', end='2023-10-09 05:00:00', freq='h').strftime('%H').astype(int)})

    # Merge hourly_avg_sentiment with all_hours
    hourly_avg_sentiment = pd.merge(all_hours, hourly_avg_sentiment, on='hour', how='left')

    return hourly_avg_sentiment

hourly_avg_sentiment = sentiment(comments)

# Plot hourly sentiment
sns.set_style('whitegrid')
sns.barplot(x='hour', y='sentiment_score', data=hourly_avg_sentiment)
plt.xlabel("Hour of the Day")
plt.ylabel("Sentiment Score")
plt.ylim(-1,1)
plt.title("Hourly Sentiment Analysis")

plt.savefig("hourly_sentiment_analysis.png")

plt.show()

