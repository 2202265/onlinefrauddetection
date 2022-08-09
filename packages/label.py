import boto3
fraudDetector = boto3.client('frauddetector')

def create_label_fraud():
    fraudDetector.put_label(
    name='fraud',
    description='label for fraud events')

def create_label_legit():
    fraudDetector.put_label(
    name='legit',
    description='label for legitimate events')

def delete_label(label_name):
    fraudDetector.delete_label(name=label_name)
