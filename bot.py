#!/usr/bin/python

import praw

GROUP_BUY = ["GROUP BUY", "GB", "GROUPBUY"]
INTEREST_CHECK = ["IC", "INTEREST CHECK", "INTERESTCHECK"]

def isGroupBuyPost(postTitle):
    postTitle = postTitle.upper()
    isGroupBuy = false
    for s in GROUP_BUY:
        if s in postTitle:
            isGroupBuy = true
    return isGroupBuy

def isInterestCheckPost(postTitle):
    postTitle = postTitle.upper()
    isInterestCheck = false
    for s in INTEREST_CHECK:
        if s in postTitle:
            isInterestCheck = true
    return isInterestCheck 

def checkRecentPosts():


def main():
    reddit = praw.Reddit('bot')
    subreddit = reddit.subreddit("mechmarket")

    groupBuyFile = open('group_buys.csv', 'a')
    interestCheckFile = open('interest_checks.csv', 'a')

    for submission in subreddit.hot(limit=5):
        print("Title: ", submission.title)
        print("URL: ", submission.url)

main()
