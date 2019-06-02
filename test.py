import requests
import praw
import subs
import json
from credentials import *
from requests import Session

for user in users:
	for x in subs:
		reddit = praw.Reddit(
			client_id=user['client_id'],
			client_secret=user['client_secret'],
			user_agent=user['user_agent'],
			username=user['username'],
			password=user['password'],
	    )
		url = 'https://www.tits.com'
		title = 'titty docs'
		reddit.subreddit(x).submit(title, url=url)
				

# url = 'https://httpbin.org/ip'
# proxies = {
#     'https':
# }
# for p in proxies.values():
# 	print(p)
# reddit = praw.Reddit()
# max_posts = 20



