1. All the python scripts and supporting files are placed inside folder - 'source code'.
2. Please refer to the document 'GCP-steps.pdf' for detailed description of the steps mentioned below.

Following steps are to be done to implement sentiment analysis on GCP:
1. Create a project on GCP and Create a VM instance on GCP under this project
2. SSH to the created instance and carry out required installations like pip3,python3,jdk-latest,google-cloud (refer GCP-steps.pdf document). 
3. Enable the Cloud NLP API and create the necessary service account for it.
4. Create a topic in pub/sub (analysereddit-topic) to ingest reddit comments.
5. Create a Cloud function subscribed to above topic. Paste code in sentiment_cloudfunction.py file into the cloud function console source.
   Add contents of requirements.txt in requirements.txt file of the cloud function.
6. Now in VM instance run 'publisher_reddit.py' script with a Reddit URL as input.
7. The results of the sentiment analysis of the reddit comments will be available in 'Log Viewer' inside the 'Operations Logging' component of the project.
   The text for each comment and their corresponding score and magnitude will be visible in logs.
8. In the VM instance, carry out the installations and configurations needed for Logstash, Elasticsearch and Kibana  (refer GCP-steps.pdf document).
9. Create a topic (elk-topic2) in Pub/Sub. 
10. Create a 'Sink' (elk-sink2) in 'Log Router' component of Logs with destination as above created topic with inclusion filter of the created cloud Function.
   This will export the logs to the topic.
11. Create a 'Pull' type subscription (elk-subscription-topic2) on above (elk-topic2) topic.
12. Carry out the installations for Beats - 'pubsubbeats'.
13. Define and upload ingest Pipeline to elasticsearch. (refer document - GCP-setup.pdf).
14. Make necessary changes in pubsubbeat.yml file and Start the Beat.
15. Now the Logs will get exported to Elasticsearch and new index will be created in Elasticsearch.
16. Login to Kibana to view the Logs under 'Discover' Option.
17. Create visualizations based on Scores using 'Visualize' option in Kibana.

References for pubsubbeat implementation : https://github.com/googlearchive/pubsubbeat

