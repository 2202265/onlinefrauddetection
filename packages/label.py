import boto3
fraudDetector = boto3.client('frauddetector')

def create_label_fraud():
    fraudDetector.put_label(
    name='fraud',
    description='fraud')

def create_label_legit():
    fraudDetector.put_label(
    name='legit',
    description='legit')
