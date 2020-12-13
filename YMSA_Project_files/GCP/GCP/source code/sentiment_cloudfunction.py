def sentiment_cloudfunction(data, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         data (dict): The dictionary with data specific to this type of event.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata.
    """
    import base64
    from google.cloud import language_v1

    post = ''
    
    if 'data' in data:
        try:
            post = base64.b64decode(data['data']).decode('utf-8')
        except Exception:
            post = data['data']
            print('not base64 encoded')
            pass

    # print('Hello {}!'.format(post))
    """Run a sentiment analysis request on text within a passed filename."""
    client = language_v1.LanguageServiceClient()

    text = post

    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    encoding_type = language_v1.EncodingType.UTF8
    annotations = client.analyze_sentiment(document=document)


    score = annotations.document_sentiment.score
    adjusted_score = (score + 1) * 5
    magnitude = annotations.document_sentiment.magnitude
    import json
    #dic = {"post": str(post), "score": str(adjusted_score), "magnitude": str(magnitude)}
    dic = {"post": str(post), "score": (adjusted_score), "magnitude": (magnitude)}
    print(json.dumps(dic))