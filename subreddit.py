# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:38:02 2020

@author: harsh
"""

import praw
import re
import os
from praw.models import MoreComments

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)
# create a file to store the parsed comments
if os.path.isfile('output.txt'):
    f = open("output.txt", "a+", encoding = 'utf-8')
else:
    f = open("output.txt", "w+", encoding = 'utf-8') 
# giving in credentials for accessing the reddit data   
# refer the readme to access your credentials
# register though the given link and then fill in your credentials
reddit = praw.Reddit(user_agent="Comment Extraction (by /u/USERNAME)",
                      client_id="14 digit code", client_secret="27 digit code",
                      username="user_name", password="password")
subreddit = reddit.subreddit('subreddit').hot(limit=10)
subreddit = list(subreddit)
for post in subreddit[2:]:
  submission = reddit.submission(id=post.id)
  submission.comments.replace_more(limit=0)
  for comment in submission.comments.list():
      p = comment.body.encode('utf-8')
      p = str(p.decode(encoding = 'utf-8'))
#    if type(i)!= 'bytes':
      f.write(deEmojify(p))
      f.write('\n')




