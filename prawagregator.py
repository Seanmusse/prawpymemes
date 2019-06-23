import praw
import os
import urllib.request
import smtplib
import string
import subprocess
import sys
from credentials import *

reddit = praw.Reddit(client_id = r_client_id,
                     client_secret = r_client_secret,
                     user_agent = "pymemeaggregator v0.1 (by /u/similarlanguage)")

#list of subreddits that will be searched for memes
subs = (
        "MemeEconomy",
        "dankmemes",
        "memes",
        "cursedimages",
        "blursedimages",
        "dankchristianmemes",
        "bonehurtingjuice",
        "HistoryMemes",
        "renaissancememes"
)

#supported file formats
file_formats = ("jpg", "png")

sub_list = []
path = "/home/gravatio/programming/python/projects/pymemes/images4drive"
for sub in subs:
    for submission in reddit.subreddit(sub).top("day", limit=5):
        if submission.url[-3::] in file_formats:
            print(submission.url)
            sub_list.append(submission.url)
            for meme in sub_list:
                urllib.request.urlretrieve(meme, os.path.join(path, os.path.basename(meme)))

        else:
            pass

    print(" ")
    print("-----" + sub + "------")
    print(" ")


# setting up the server

os.chdir(path)
subprocess.run([sys.executable, "-m", "http.server"])
