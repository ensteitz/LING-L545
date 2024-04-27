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



'''
OLD code. Picked and chose from this. Will clean it up later.

import praw
import pandas as pd
from datetime import datetime as dt
from praw.models import MoreComments


reddit = praw.Reddit(
        client_id="9eaZgAHFqJAkFbK6fFJAMg", 
        client_secret="o1hw9hNDdt_JfYQJg0_37A2lwaQ6gA", 
        password="password",
        user_agent="Project to analyze public sentiment about the Israel/Palestine"
	)
print(reddit)

posts = []
# Add an empty data variable to store all the data to be used for pandas
attributes_dict = { "title":[],
                "score":[],
                "id":[], "url":[],
                "comms_num": [],
                "created": [],
                "body":[]}

subreddit = reddit.subreddit('r/AmericanPolitics')
print(subreddit)
submission = reddit.submission("1c019n5")
# Avoid the 'MoreComments' common error
#submission.comments.replace_more(limit=None)
print(submission.comments)
# Iterate over the comments in the specific post to get each one
for comment in submission.comments.list():
        attributes_dict["title"].append(submission.title)
        attributes_dict["score"].append(submission.score)
        attributes_dict["id"].append(submission.id)
        attributes_dict["url"].append(submission.url)
        attributes_dict["comms_num"].append(submission.num_comments)
        attributes_dict["created"].append(submission.created)
        attributes_dict["body"].append(submission.selftext)
        posts.append(attributes_dict)
        attributes_data = pd.DataFrame(attributes_dict)
        print("up to here")
        print(comment.body)

attributes_data = pd.DataFrame(attributes_dict)

def get_date(created):
    return dt.fromtimestamp(created)

_timestamp = attributes_data["created"].apply(get_date)
topics_data = attributes_data.assign(timestamp = _timestamp)
'''
