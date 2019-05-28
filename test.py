import praw
from credentials import *

my_reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

subs = [
	'barstoolsports',
	'technology',
	'rap'
]
max_posts = 20

for s in subs:
	for submission in my_reddit.subreddit(s).new(limit=max_posts):
		print(submission.title)