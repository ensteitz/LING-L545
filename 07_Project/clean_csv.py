import sys
import pandas as pd

# Using the data from the newly created CSV
file_path = 'df_comments.csv'

df = pd.read_csv(file_path)

#df['body'] = df['body'].str.lstrip('>')

# Phrases I want gone
phrases_to_search = [
    "Please avoid using profanities to make a point or emphasis",
    "https://",
    "this action was performed automatically",
    "I am a bot",
    "comments and analogies are inflammatory",
    "post is getting locked"
]

# Reg ex to match any of the phrases
pattern = '|'.join(phrases_to_search)

# Get rid of rows w/ any of the specified phrases
df_clean = df[~df['body'].str.contains(pattern, case=False, na=False)]

df_clean.to_csv('df_clean_comments.csv', index=False)

print(df_clean)
