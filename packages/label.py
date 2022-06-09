import boto3
fraudDetector = boto3.client('frauddetector')

def create_label():
    fraudDetector.put_label(
    name='string',
    description='string')
