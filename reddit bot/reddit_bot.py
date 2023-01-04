import os
import praw


reddit = praw.Reddit(
    client_id="IyxtX-bFcdUxcQ",
    client_secret="nP1VSdqoxniPuKEC11zAKiB4W0M",
    username="lord_white_knight",
    password="Lord792002",
    redirect_uri="http://localhost:8080",
    user_agent="test script by-/u/jussi-boe")
print(reddit.auth.url(["identity"], "...", "permanent"))

def check_file(file, comment_id):
    with open(file) as f:
       if comment_id in f.read().split('\n'):
          return True
       else:
          f.write(comment_id+'\n')
          return False

def run_bot(): #make the file name a function variable
    for comment in reddit.subreddit('YOURSUBREDDIT').stream.comments():
        if 'EXPRESSION' in comment.body and check_file('records.txt',comment_id) is False:
            comment.reply('REPLY')

print(reddit.user.me())
