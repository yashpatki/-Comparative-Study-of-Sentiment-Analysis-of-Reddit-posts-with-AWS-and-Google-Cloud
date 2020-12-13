
import os
import praw
import argparse
import json
import boto3
import re


os.environ["REDDIT_CLIENT_ID"] = ""
os.environ["REDDIT_CLIENT_SECRET"] = ""
os.environ["REDDIT_USERNAME"] = ""
os.environ["REDDIT_USER_AGENT"] = ""
os.environ["REDDIT_PASSWORD"] = ""

session = boto3.Session(profile_name='default')
temperatureClient = session.client('firehose')
s3 = boto3.resource('s3')

comprehend = boto3.client(service_name='comprehend', region_name='us-east-2')
kinesis = boto3.client(service_name='firehose', region_name='eu-west-1')

reddit = praw.Reddit(
    client_id=os.environ['REDDIT_CLIENT_ID'],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
)


parser = argparse.ArgumentParser()
parser.add_argument('url')
parser.add_argument('--threshold', default=.8, type=float)
args = parser.parse_args()

submission = reddit.submission(url=args.url)
print('{} - by {}'.format(submission.title, submission.author))
submission.comments.replace_more(limit=None)

comments = submission.comments.list()
print('{} comments'.format(len(comments)))

c = " "
for comment in comments:
    if(len(c) > 4200):
        break
    else:
        c = c + " " + str(comment.body)
comment1 = c
omment1 = re.sub(
    u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])', '', comment1)
comment1 = re.sub(r"(?:X|:|;|=)(?:-)?(?:\)|\(|O|D|P|S){1,}", '', comment1)
comment1 = re.sub(r'^(RT|FAV)', '', comment1)
comment1 = re.sub(r"(^|\s)(\-?\d+(?:\.\d)*|\d+)", '', comment1)
comment1 = re.sub(r':', '', comment1)

s3.Object('cloud-project-bucket-2', 'trial.txt').put(Body=comment1)
