#!/usr/bin/python

import praw

reddit = praw.Reddit('bot')

subreddit = reddit.subreddit("mechmarket")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("URL: ", submission.url)
