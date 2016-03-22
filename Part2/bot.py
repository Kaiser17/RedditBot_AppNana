import praw

import pdb
import re
import os
from config_bot import *

if not os.path.isfile("config_bot.py"):
    print "You must create a config file."
    print "Please see config_skel.py"
    exit(1)

ua = ("PyAppNana v.1")
r = praw.Reddit(user_agent = ua)


if not os.path.isfile("posts_replied_to.txt"):
  prt = []
else:
  with open("posts_replied_to.txt"):
    prt = f.read()
    prt = prt.split("\n")
    prt = prt.filter(None, prt)

#subreddit = r.get_subreddit("AppNana")
subreddit = r.get_subreddit("pythonforengineers")

for sub in subreddit.get_hot(limit = 5):
  print "Title: ", sub.title

  if sub.id not in prt:
    if not re.search("j11914088", submission.title, re.IGNORECASE):
      sub.add_comment("I added you, if you can please add me back! (j11914088)")

  print "-"*40+"\n" 

