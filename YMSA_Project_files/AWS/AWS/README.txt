The steps to follow to run the Reddit sentiment analysis application on AWS


- Configure and launch EC2 Linux instance
- Install Python 3.6+
commands - sudo yum install python36
           sudo yum install python36-pip
- Set python 3 as default
command - sudo update-alternatives --config python
- Install boto3
command - sudo pip install boto3
- Create an S3 bucket to store all the Reddit comments
- Create a Kinesis Firehose delivery stream and choose Source as the s3 bucker created in the previous step.
- Create Lambda function on AWS which gets triggered every time data is written into the s3 bucket and using AWS comprehend API to retrieve the sentiment of the comments
- Create a domain in Elastic Search Service with index as Comment and type as comment.Choose t2.small.elasticsearch as instance type and version as 6.5
- Copy the comments_reddit.py file onto the ec2 instance and run it using the command python comments_reddit.py
- Application logs from the lambda function are stored in CloudWatchLogs.
- These logs are used by the elastic search for visualisation.
- The data stored can be viewed by visiting the indices tab on the elastic search dashboard.
- Graphs can be created for visualisation using the Kibana Visualisation tool which is automatically deployed with an elastic search domain.