import json
import boto3
import urllib

def lambda_handler(event, context):
	s3 = boto3.client("s3")
	bucket = "bucket name"
	key = record[0]['s3']['object']['key']
	file = s3.get_object(Bucket = bucket,Key = key)
	paragraph = str(file['Body'].read())
	comprehend = boto3.client("comprehend")
	response = comprehend.detect_sentiment(Text = paragraph, LanguageCode = 'en')

	return response