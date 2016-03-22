import praw

ua = ("PyAppNana v.1")
r = praw.Reddit(user_agent = ua)

#subreddit = r.get_subreddit("AppNana")
subreddit = r.get_subreddit("pythonforengineers")

for sub in subreddit.get_hot(limit = 5):
  print "Title: ", sub.title
  print "-"*40+"\n" 
