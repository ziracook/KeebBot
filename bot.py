#!/usr/bin/python

import praw
import csv
import pprint

GROUP_BUY = ["[GB]", "GROUP BUY", "GROUPBUY"]
INTEREST_CHECK = ["[IC]", "INTEREST CHECK", "INTERESTCHECK"]
groupBuys = dict()
interestChecks = dict()

def isGroupBuyPost(postTitle):
    postTitle = postTitle.upper()
    isGroupBuy = False
    for s in GROUP_BUY:
        if s in postTitle:
            isGroupBuy = True
    return isGroupBuy

def isInterestCheckPost(postTitle):
    postTitle = postTitle.upper()
    isInterestCheck = False
    for s in INTEREST_CHECK:
        if s in postTitle:
            isInterestCheck = True
    return isInterestCheck 

def appendDiciontaryToCsv(fileName, dictionary):
    with open(fileName, 'a', newline='') as csvfile:
        fieldnames = ['postTitle', 'postURL']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()    
        
        for title, url in dictionary.items():
            csvwriter.writerow({'postTitle': title, 'postURL': url})

def main():
    reddit = praw.Reddit('bot')
    subreddit = reddit.subreddit("mechmarket")
    postsChecked = 0

    for post in subreddit.hot(limit=20):
        postsChecked += 1  
        if isGroupBuyPost(post.title):
            groupBuys[post.title] = post.url
        elif isInterestCheckPost(post.title):
            interestChecks[post.title] = post.url 
    print(postsChecked)

main()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(groupBuys)
pp.pprint(interestChecks)

