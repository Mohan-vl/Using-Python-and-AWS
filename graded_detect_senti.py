import boto3
import json

def lambda_handler(event,context):
    s3 = boto3.client("s3")
    bucket = "testbuck-3"
    key = "Graded_Review_Analysis.txt"
    file = s3.get_object(Bucket = event['bucket'], Key = event['object_name'])
    paragraph = str(file['Body'].read())
        
    comprehend = boto3.client('comprehend')
    
    sentiment = comprehend.detect_sentiment(Text = paragraph, LanguageCode = "en")
    
    return (sentiment['Sentiment'])


