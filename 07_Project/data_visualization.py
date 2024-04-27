import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ast
plt.rcParams['lines.markersize'] = 2

# Load the CSV file into a DataFrame
df = pd.read_csv("df_sa_extralabels_clean_comments.csv")

# Data Exploration
print(df.head())  # Check the first few rows of the DataFrame
print(df.info())  # Get information about the DataFrame

# Data Visualization

# 1. Bar Plot: Number of Comments by Time of Day
sns.countplot(x='time_of_day', data=df)
plt.title('Number of Comments by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Number of Comments')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.savefig('comments_by_time_of_day.png')  # Save the plot as an image file
plt.close()

# 2. Histogram: Distribution of Upvotes
sns.histplot(df['upvotes'], bins=20)
plt.title('Distribution of Upvotes')
plt.xlabel('Upvotes')
plt.xlim(-20, 25)
plt.ylabel('Frequency')
plt.savefig('upvotes_distribution.png')  # Save the plot as an image file
plt.close()

# 2.5 Box Plot
sns.boxplot(x='upvotes', data=df)
plt.title('Distribution of Upvotes')
plt.xlabel('Upvotes')
plt.xlim(-10, 15)
plt.savefig('upvotes_boxplot.png')  # Save the plot as an image file
plt.close()

# 3. Box Plot: Upvotes by Time of Day
sns.boxplot(x='time_of_day', y='upvotes', data=df)
plt.title('Upvotes by Time of Day')
plt.xlabel('Time of Day')
plt.ylim(-10, 25)
plt.ylabel('Upvotes')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.savefig('upvotes_by_time_of_day.png')  # Save the plot as an image file
plt.close()

# 4. Scatter Plot: Upvotes vs. Sentiment Score
sns.scatterplot(x='upvotes', y='sentiment_scores', data=df)
plt.title('Upvotes vs. Sentiment Score')
plt.xlabel('Upvotes')
plt.xlim(-10, 30)
plt.ylabel('Sentiment Score')
plt.savefig('upvotes_vs_sentiment_score.png')  # Save the plot as an image file
plt.close()

# 4.5 Scatter Plot: Upvotes vs. Compound Sentiment Score
import ast  # Import ast module to handle string to dictionary conversion

# Load the CSV file into a DataFrame
comments = pd.read_csv("df_sa_extralabels_clean_comments.csv")

# Convert the string representation of sentiment scores to dictionaries
comments["sentiment_scores"] = comments["sentiment_scores"].apply(ast.literal_eval)

# Create a new column "compound_score" by extracting the "compound" value from "sentiment_scores"
comments["compound_score"] = comments["sentiment_scores"].apply(lambda x: x["compound"])

# Scatter Plot: Upvotes vs. Compound Sentiment Score
sns.scatterplot(x='upvotes', y='compound_score', data=comments)
plt.title('Upvotes vs. Compound Sentiment Score')
plt.xlabel('Upvotes')
plt.xlim(-15,20)
plt.ylabel('Compound Sentiment Score')
plt.savefig('upvotes_vs_compound_sentiment_score.png')  # Save the plot as an image file
plt.close()

# 5. Pair Plot: Pairwise Relationships
sns.pairplot(df[['upvotes', 'hour', 'sentiment_scores']])
plt.title('Pairwise Relationships')
plt.savefig('pairwise_relationships.png')  # Save the plot as an image file
plt.close()




'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv("df_sa_extralabels_clean_comments.csv")

# Data Exploration
print(df.head())  # Check the first few rows of the DataFrame
print(df.info())  # Get information about the DataFrame

# Data Visualization

# 1. Bar Plot: Number of Comments by Time of Day
sns.countplot(x='time_of_day', data=df)
plt.title('Number of Comments by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Number of Comments')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# 2. Histogram: Distribution of Upvotes
sns.histplot(df['upvotes'], bins=20)
plt.title('Distribution of Upvotes')
plt.xlabel('Upvotes')
plt.ylabel('Frequency')
plt.show()

# 3. Box Plot: Upvotes by Time of Day
sns.boxplot(x='time_of_day', y='upvotes', data=df)
plt.title('Upvotes by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Upvotes')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# 4. Scatter Plot: Upvotes vs. Sentiment Score
sns.scatterplot(x='upvotes', y='sentiment_scores', data=df)
plt.title('Upvotes vs. Sentiment Score')
plt.xlabel('Upvotes')
plt.ylabel('Sentiment Score')
plt.show()

# 5. Pair Plot: Pairwise Relationships
sns.pairplot(df[['upvotes', 'hour', 'sentiment_scores']])
plt.title('Pairwise Relationships')
plt.show()
'''
