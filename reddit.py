#!/usr/bin/python3

import requests, OAuth2, praw, datetime

#useragent
r = praw.Reddit("My Python Personal CLI Scraper for Reddit v.1.0 (by /u/dtech12)")

#authorize the reddit script from reddi's API so that we can CALL to it.
r.set_oauth_app_info(OAuth2.app_id, OAuth2.app_secret, OAuth2.app_uri)

#take input from the user as a reddit username
reddit_user = input("Enter a reddit username: ")

#look up reddit username
user = r.get_redditor(reddit_user)

timestamp = user.created_utc

#'humanize' timestamp
date = datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%B %d, %Y')

#user info
link_karma = user.link_karma
comment_karma = user.comment_karma
comments = user.get_comments(limit=None)
posts = user.get_submitted(limit=None)

print ()
print ("[x] [your name here], this is what I have for " + reddit_user + ":")
print ("[x] " + reddit_user + " registered on " + str(date) + ".")
print ("[x] " + (str(link_karma) + " Link Karma"))
print ("[x] " + (str(comment_karma) + " Comment Karma"))
print ("[x] " + (str(len(list(comments))) + " Comments"))
print ("[x] " + (str(len(list(posts))) + " Posts"))
print
print ("[*] " + reddit_user + "'s five most recent posts were:")
print ()
for submission in user.get_submitted(sort='new', time='all', limit=5):
    print ("	[>] " + str(submission))

print ()
print ("[*] " + reddit_user + "'s five most recent comments were:")
print ()
for comment in user.get_comments(sort='new', time='all', limit=5):
    print ("	[>] " + comment.body)
print ()
print ()
