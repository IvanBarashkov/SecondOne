import boto3
import os

ec2 = boto3.resource('ec2')

lt = {
    'LaunchTemplateName': os.environ['TEMPLATE_NAME'],
    'Version': '$Latest'
}

def lambda_handler(event, context):

    instances = ec2.create_instances(
        LaunchTemplate=lt,
        MinCount=1,
        MaxCount=1
    )
