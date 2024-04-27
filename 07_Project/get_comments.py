import praw
import pandas as pd
from datetime import datetime as dt

# Set up id and verify it
reddit = praw.Reddit(client_id="9eaZgAHFqJAkFbK6fFJAMg",
	client_secret="o1hw9hNDdt_JfYQJg0_37A2lwaQ6gA",
	password="password",
	user_agent="Final project to analyze public sentiment about the conflict in Israel/Palestine, username=fallenfloral")

# Add an empty data variable to store all the data to be used for pandas
attributes_dict = { "id":[],
        "author":[],
        "body":[],
        "upvotes": [],
        "created": [],
        "parent_id": []}

# Specify which submission will be analyzed
# This is the post titled "I have changed my mind about the Israel-Palestine conflict. Have you?"
submission = reddit.submission("172w9gt")

# Avoid the 'MoreComments' common error
submission.comments.replace_more(limit=None)

# Create a variable to store the text of the reddit post (comments and replies)
f = open("comments.txt", "w")

test_c = 0

test_r = 0

# Iterate over the comments in the specific post to get each original comment
for comment in submission.comments.list():
	if comment.body in attributes_dict["body"]: continue
	attributes_dict["id"].append(comment.id)
	attributes_dict["author"].append(comment.author.name if comment.author else "[deleted]")
	attributes_dict["body"].append(comment.body)
	attributes_dict["upvotes"].append(comment.score)
	attributes_dict["created"].append(comment.created_utc)
	attributes_dict["parent_id"].append(comment.parent().id)  # Store the parent comment ID
	print(comment.body, file=f)
	test_c = test_c + 1

	# Iterate through the original comments to get all the embedded comments
	for reply in comment.replies:
		if reply.body in attributes_dict["body"]: continue
		attributes_dict["id"].append(reply.id)
		attributes_dict["author"].append(reply.author.name if reply.author else "[deleted]")
		attributes_dict["body"].append(reply.body)
		attributes_dict["upvotes"].append(reply.score)
		attributes_dict["created"].append(reply.created_utc)
		attributes_dict["parent_id"].append(reply.parent().id)  # Store the parent comment ID
		test_r = test_r + 1
		print(reply.body, file=f)
print(test_c)
print(test_r)

# Create a dataframe
attributes_data = pd.DataFrame(attributes_dict)

def get_date(created):
	return dt.fromtimestamp(created)

attributes_data["timestamp"] = attributes_data["created"].apply(get_date)

print(attributes_data)

# Close the file
f.close()

# Export the data to a csv file
# The csv file will then go through cleaning, so this is just the initial data csv file
attributes_data.to_csv('df_comments.csv', index=False)




# This file was renamed from reddit_data545.py
