import sys
import pandas as pd

# Assuming df_comments.csv is in the same directory as your Python script
file_path = 'df_comments.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

#df['body'] = df['body'].str.lstrip('>')

# Define the phrases to search for
phrases_to_search = [
    "Please avoid using profanities to make a point or emphasis",
    "https://",
    "this action was performed automatically",
    "I am a bot",
    "comments and analogies are inflammatory",
    "post is getting locked"
]

# Create a regular expression pattern to match any of the phrases
pattern = '|'.join(phrases_to_search)

# Filter the DataFrame to remove rows containing any of the specified phrases
df_clean = df[~df['body'].str.contains(pattern, case=False, na=False)]

# Save the filtered DataFrame back to a CSV file
df_clean.to_csv('df_clean_comments.csv', index=False)

# Optionally, print the filtered DataFrame
print(df_clean)







'''
#first, explore what strings you want to remove by identifying tagwords
# i.e. "This is a bot" "comment removed", etc.
# take those statements and use them here with code to remove them from not just the text file but also the csv
'''