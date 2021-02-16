import boto3
import json
import os

sns_arn = os.environ['SNS_TOPIC_ARN']
custom_subject = os.environ['CUSTOM_SUBJECT']

def lambda_handler(event, context):
    print(sns_arn)
    client = boto3.client("sns")
    resp = client.publish(TargetArn=sns_arn, Message=json.dumps(event), Subject=custom_subject)

