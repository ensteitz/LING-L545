import praw
import pandas as pd
from datetime import datetime as dt


reddit = praw.Reddit(
        client_id="9eaZgAHFqJAkFbK6fFJAMg", \
        client_secret="o1hw9hNDdt_JfYQJg0_37A2lwaQ6gA", \
        password="password", \
        user_agent="Project to analyze public sentiment about the Israel/Palestine, username=fallenfloral")

# Add an empty data variable to store all the data to be used for pandas
attributes_dict = { "id":[],
	"author":[],
	"body":[],
	"upvotes": [],
	"created": [],
	"parent_id": []}

submission = reddit.submission("1bk96ug")

# Avoid the 'MoreComments' common error
submission.comments.replace_more(limit=None)


# Iterate over the comments in the specific post to get each one
for comment in submission.comments.list():
	attributes_dict["id"].append(comment.id)
	attributes_dict["author"].append(comment.author.name if comment.author else "[deleted]")
	attributes_dict["body"].append(comment.body)
	attributes_dict["upvotes"].append(comment.score)
	attributes_dict["created"].append(comment.created_utc)
	attributes_dict["parent_id"].append(comment.parent().id)  # Store the parent comment ID

	# Iterate through replies for this comment
	for reply in comment.replies:
		attributes_dict["id"].append(reply.id)
		attributes_dict["author"].append(reply.author.name if reply.author else "[deleted]")
		attributes_dict["body"].append(reply.body)
		attributes_dict["upvotes"].append(reply.score)
		attributes_dict["created"].append(reply.created_utc)
		attributes_dict["parent_id"].append(reply.parent().id)  # Store the parent comment ID
		print("Comment reply attributes added")

#create a dataframe
attributes_data = pd.DataFrame(attributes_dict)

def get_date(created):
    return dt.fromtimestamp(created)

attributes_data["timestamp"] = attributes_data["created"].apply(get_date)

print(attributes_data)

attributes_data.to_csv('FILENAME.csv', index=False)
