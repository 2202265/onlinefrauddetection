import boto3
fraudDetector = boto3.client('frauddetector')

def create_label(label_name,label_description):
    fraudDetector.put_label(
    name=label_name,
    description=label_description)

def delete_label(label_name):
    fraudDetector.delete_label(name=label_name)
