# [start imports]
import argparse
import os
import praw
import json
import re
from google.cloud import pubsub_v1
# [end imports]

# [variable settings start]
project_id = "reddit-nlp-296707"
topic_name = "analysereddit-topic"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

# [START set reddit variables]
os.environ["REDDIT_CLIENT_ID"] = ""
os.environ["REDDIT_CLIENT_SECRET"] = ""
os.environ["REDDIT_USERNAME"] = ""
os.environ["REDDIT_USER_AGENT"] = "CloudComputing"
os.environ["REDDIT_PASSWORD"] = ""
reddit = praw.Reddit(
    client_id=os.environ['REDDIT_CLIENT_ID'],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
)
# [END set reddit variables]


def callback(message_future):
    # When timeout is unspecified, the exception method waits indefinitely.
    if message_future.exception(timeout=30):
        print('Publishing message on {} threw an Exception {}.'.format(
            topic_name, message_future.exception()))
    else:
        print('result=' + message_future.result())


def publish_to_pubsub(rpost):
    # Data must be a byte string
    rpost = rpost.encode('utf-8')
    # When you publish a message, the client returns a Future.
    message_future = publisher.publish(topic_path, data=rpost)
    message_future.add_done_callback(callback)


parser = argparse.ArgumentParser()
parser.add_argument('url')
parser.add_argument('--threshold', default=.8, type=float)
args = parser.parse_args()
count = 0
submission = reddit.submission(url=args.url)
submission.comments.replace_more(limit=None)

for comment in submission.comments.list():
    content = str(comment.body)
    content = re.sub(
        u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])', '', content)
    content = re.sub(r"(?:X|:|;|=)(?:-)?(?:\)|\(|O|D|P|S){1,}", '', content)
    content = re.sub(r'^(RT|FAV)', '', content)
    content = re.sub(r"(^|\s)(\-?\d+(?:\.\d)*|\d+)", '', content)
    print(content)
    publish_to_pubsub(content)
    count = count+1
    print(count)
